# coding:utf-8
__author__ = 'frkhit'

import datetime

from celery import Celery
from celery.schedules import crontab

from celery_proj import basic_config

basic_config.CELERYBEAT_SCHEDULE = {
    'trigger_minute_clock': {
        'task': 'tasks.trigger_minute_clock',
        'schedule': crontab(minute="*/1"),
    },
    'trigger_minute_notice': {
        'task': 'tasks.trigger_minute_notice',
        'schedule': crontab(minute="*/2", )
    },
}
QUEUE_SCHEDULE_DEFAULT = "main-schedule"
basic_config.CELERY_TASK_DEFAULT_QUEUE = QUEUE_SCHEDULE_DEFAULT
basic_config.CELERY_TASK_CREATE_MISSING_QUEUES = True

APP_NAME = 'scheduler_main'
app = Celery(APP_NAME)
app.config_from_object(basic_config)

app.conf.task_routes = {'tasks.*': {'queue': QUEUE_SCHEDULE_DEFAULT}}


@app.task(name="tasks.trigger_minute_clock")
def print_time():
    print("[print time] msg is {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


@app.task(name="tasks.trigger_minute_notice")
def send_notice():
    print("[send notice] msg is {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
