import re
import subprocess 
import shlex 
import time

from django.conf import settings
from django.utils import timezone
from mission_report import parse_mission_log_line
from stats.models import Profile, ProfileStats
from stats.logger import logger

USER_CONNECTED = 1
USER_DISCONNECTED = 2
SERVER_IP = settings.GAME_SERVER_IP
SERVER_PORT = settings.GAME_SERVER_PORT

# Крылья Онлайн: список активных соединений
def get_stats(server_ip, server_port):
    ips = []

    netstat = subprocess.Popen(shlex.split('netstat -an -p TCP'), stdout=subprocess.PIPE)    
    grep_established = subprocess.Popen(shlex.split('grep ESTABLISHED'), stdin=netstat.stdout, stdout=subprocess.PIPE)
    grep_ip = subprocess.Popen(shlex.split("grep %s:%s" % (server_ip, server_port)), stdin=grep_established.stdout, stdout=subprocess.PIPE)

    while True:
        output = grep_ip.stdout.readline().decode("utf-8")
        if output != '':
            m = re.match(r"\s+TCP\s+[\d\.:]+\s+(?P<ip>[\d\.]+):", output, re.IGNORECASE)            
            if m:
                ip = m.group('ip')
                ips.append(ip)
        else:
            break

    return ips

# Крылья Онлайн: cравнение двух списков, list1 - список для проверки
def compare_lists(list1, list2):
    diff_elements = []

    for element in list1:
        if element not in list2:
            diff_elements.append(element)

    return diff_elements

# Крылья Онлайн: профайл игрока
def get_profile_id(uuid):
    try:
       profile = Profile.objects.get(uuid=uuid)
    except Profile.DoesNotExist:
       profile = None

    if profile:
        return profile.id

def update_profile_stats(m_report_files, prev_connected):
    connected = get_stats(SERVER_IP, SERVER_PORT)
    new_logged_connects = []
    new_logged_disconnects = []

    file_path = m_report_files[-1]

    if time.time() - file_path.stat().st_mtime < 120:
        for line in file_path.open():
            if 'AType' not in line:
                logger.warning('ignored bad string: [{}]'.format(line))
                continue
            try:
                data = parse_mission_log_line.parse(line)
            except parse_mission_log_line.UnexpectedATypeWarning:
                logger.warning('unexpected atype: [{}]'.format(line))
                continue

            atype_id = data.pop('atype_id')

            if atype_id == 20 and data['tik'] != 0:
                profile_id = get_profile_id(data['account_id'])
                if profile_id:
                    new_logged_connects.append(profile_id)
            elif atype_id == 21:
                profile_id = get_profile_id(data['account_id'])
                if profile_id:
                    new_logged_disconnects.append(profile_id)

        new_connects = compare_lists(connected, prev_connected)
        new_disconnects = compare_lists(prev_connected, connected)
        
        if len(new_logged_connects) == 1 and len(new_connects) == 1 and len(new_logged_disconnects) == 0 and len(new_disconnects) == 0:
           ProfileStats.objects.get_or_create(profile_id=new_logged_connects[0], ip=new_connects[0], type=USER_CONNECTED, connection_date=timezone.now())
        if len(new_logged_disconnects) == 1 and len(new_disconnects) == 1 and len(new_logged_connects) == 0 and len(new_connects) == 0:
           ProfileStats.objects.get_or_create(profile_id=new_logged_disconnects[0], ip=new_disconnects[0], type=USER_DISCONNECTED, connection_date=timezone.now())

    return connected