import filelock
from django.conf import settings
from django.core.management.base import BaseCommand
from stats import netstat
from stats.logger import logger


class Command(BaseCommand):

    def handle(self, *args, **options):
        lock = filelock.FileLock(str(settings.BASE_DIR.parent.joinpath('netstat.lock')), timeout=5)
        with lock:
            try:
                netstat.main()
            except Exception:
                logger.exception('unexpected error')
                raise
