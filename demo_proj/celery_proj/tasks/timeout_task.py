# -*- coding: utf-8 -*-

import time

from celery.exceptions import SoftTimeLimitExceeded

from celery_proj.app import celery_app
from libs.demo_utils import simple_log, celery_task_logger


@celery_app.task(soft_time_limit=3, ignore_result=True, bind=True)
@celery_task_logger
@simple_log
def timeout_task(self, sleep_time: int):
    try:
        time.sleep(sleep_time)
    except SoftTimeLimitExceeded:
        print("[task timeout error]")
