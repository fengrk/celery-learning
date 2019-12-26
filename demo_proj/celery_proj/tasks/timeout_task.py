# -*- coding: utf-8 -*-

import time

from celery.exceptions import SoftTimeLimitExceeded

from celery_proj.app import celery_app


@celery_app.task(soft_time_limit=3, ignore_result=True)
def timeout_task(sleep_time: int):
    try:
        time.sleep(sleep_time)
    except SoftTimeLimitExceeded:
        print("[task timeout error]")
