import subprocess 
import shlex 

from stats.logger import logger

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)    
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            log = output.strip()
            logger.info('{info}'.format(info=output.strip()))
    rc = process.poll()
    return rc

def main():
    run_command('netstat -a')

main()