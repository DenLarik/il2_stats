import logging
import re
import time

from mission_report import parse_mission_log_line
from stats.models import CurrentMission


logger = logging.getLogger('current_mission')


def update_current_mission(m_report_files):
    try:
        current_mission = CurrentMission.objects.all()[0]
    except IndexError:
        current_mission = None

    if current_mission:
        duration = time.time() - m_report_files[0].stat().st_mtime
        CurrentMission.objects.update(duration=duration);
    else:
        for line in m_report_files[0].open():
            if 'AType' not in line:
                logger.warning('ignored bad string: [{}]'.format(line))
                continue
            try:
                data = parse_mission_log_line.parse(line)
            except parse_mission_log_line.UnexpectedATypeWarning:
                logger.warning('unexpected atype: [{}]'.format(line))
                continue

            atype_id = data.pop('atype_id')

            if atype_id == 0:
                mission = 'Unknown'
                m = re.match(r".+\\(?P<mission>.+)[-_]WL[-_]\d+[-_]\w+.msnbin", data['file_path'], re.IGNORECASE)            
                if m:
                    mission = m.group('mission')
                CurrentMission.objects.update_or_create(name=mission, duration=0)


def cleanup_current_mission():
    CurrentMission.objects.all().delete()