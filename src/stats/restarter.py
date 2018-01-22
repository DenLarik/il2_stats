import os
import subprocess
import time
from pathlib import Path

from django.conf import settings
from stats.logger import logger
from stats.models import (CurrentMission, Mission)

GAME_SERVER_PATH = settings.GAME_SERVER_PATH
GAME_SDS_PATH = '_wings_of_liberty.sds'
GAME_ROTATED_SDS_PATH = '_wings_of_liberty_rotated.sds'  #overwrited on each restart
GAME_SERVER_BIN = 'DServer.exe'
GAME_BANLIST_BIN = 'RConGen.exe'
FAILURE_TIME_OUT = 3 * 60
MAX_DURATION = 3 * 3600 + FAILURE_TIME_OUT

def stop_server(force_restart):
    if force_restart:
        os.system('taskkill /f /im ' + GAME_BANLIST_BIN)
        os.system('taskkill /f /im ' + GAME_SERVER_BIN)
    else:
        os.system('taskkill /im ' + GAME_BANLIST_BIN)
        os.system('taskkill /im ' + GAME_SERVER_BIN)

def start_server(use_rotated_sds=False):
    startup_path = Path(GAME_SERVER_PATH).joinpath('bin', 'game')
    binary_path = startup_path.joinpath(GAME_SERVER_BIN)
    sds_path = GAME_ROTATED_SDS_PATH if use_rotated_sds else GAME_SDS_PATH
    subprocess.Popen([binary_path.as_posix(), sds_path], cwd=startup_path.as_posix())
    return True

def rotate_maps(current_mission, sds_source_file, sds_target_file, skip = 0):
    """
    Reading SDS file from source file,
    rotate map order, so next map will be after line containing current_mission
    write new file to target sds file
    Example:
    source sds:
        map1
        map2
        map3
        map4
        map5
    current_mission=map3
    target sds:
        map4
        map5
        map1
        map2
        map3

    Returns False in case of problems, True if rotated successfully.
    """
    try:
        logger.info('Trying to rotate maps: current_mission={current_mission}, source_sds={source_sds}, target_sds={target_sds}'.format(
            current_mission=current_mission, source_sds=sds_source_file, target_sds=sds_target_file
        ))
        if current_mission is None:
            return False
        with sds_source_file.open(mode='r') as f:
            input = f.readlines()
        output = []
        missions_to_move = []  # missions that we want to append to back of the list
        in_rotation = False  # are we inrotation section
        before_next = True  # are we currently read line before next planned mission
        for line in input:
            if in_rotation:
                if '[end]' in line:
                    in_rotation = False
                    output.extend(missions_to_move)
                    output.append(line)
                elif line.strip().startswith('file'):
                    if before_next:
                        missions_to_move.append(line)
                    elif skip:
                        skip = skip-1
                        missions_to_move.append(line)
                    else:
                        output.append(line)
                    if current_mission in line:
                        before_next = False
                else:
                    output.append(line)
            else:
                if '[rotation]' in line:  # start rotation section
                    in_rotation = True
                output.append(line)
        # deleting previous temp file
        try:
            sds_target_file.unlink()
        except OSError:
            pass  # we are ok if file is not yet exist

        with sds_target_file.open(mode='w') as f:
            for line in output:
                f.write(line)
        logger.info("Rotated maps saved")
        return True
    except Exception as e:
        logger.info('Error rotating maps: {e}'.format(e=e))
        return False

def safe_rotate(current_mission):
    try:
        logger.info('Currrent mission = {cm}'.format(cm=current_mission))
        binary_path = Path(GAME_SERVER_PATH).joinpath('bin', 'game')  # assumption that sds file placed in game folder
        if current_mission is not None:
            return rotate_maps(current_mission.name,
                               binary_path.joinpath(GAME_SDS_PATH),
                               binary_path.joinpath(GAME_ROTATED_SDS_PATH))
        else:
            last_success_mission = Mission.objects.latest('id')
            logger.info('Last success mission = {lm}'.format(lm=last_success_mission))
            if last_success_mission is not None:
                return rotate_maps(last_success_mission.name,
                                   binary_path.joinpath(GAME_SDS_PATH),
                                   binary_path.joinpath(GAME_ROTATED_SDS_PATH), 1)
            return False
    except Exception as e:
        logger.info('Error safe rotation: {e}'.format(e=e))
        return False




def check_server(server_failure_timestamp):
    try:
        current_mission = CurrentMission.objects.all()[0]
    except IndexError:
        current_mission = None

    if current_mission is None or current_mission.duration > MAX_DURATION:
        if server_failure_timestamp == 0:
            return time.time()
        elif time.time() - server_failure_timestamp > FAILURE_TIME_OUT:
            logger.info('restarting the server...')
            logger.info('stoping the server')
            stop_server(force_restart=False)
            time.sleep(70)
            stop_server(force_restart=True)
            time.sleep(10)
            maps_rotated = safe_rotate(current_mission)
            logger.info('starting the server')
            start_server(maps_rotated)
            logger.info('restart done')
            return 0

    return server_failure_timestamp