# coding:utf-8
import os

WORKER_NAME = os.environ["WORKER_NAME"]

if __name__ == '__main__':
    with open("/run.sh", "w") as f:
        f.write('''
        #!/bin/sh
        cd /app && celery -A task worker --loglevel=info --autoscale=3,0 -n {host_name} --statedb={host_name}.state --max-tasks-per-child=100
        
        '''.format(host_name=WORKER_NAME))
