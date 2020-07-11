# -*- coding: utf-8 -*-

import time

from celery_proj.app import celery_app
from libs.demo_utils import demo_add, simple_log, celery_task_logger


@celery_app.task(bind=True)
@celery_task_logger
@simple_log
def demo_sum(self, a: float, b: float, c: float) -> float:
    time.sleep(5)
    _result = demo_add(demo_add(a, b), c)
    print("demo_sum: a {}, b {}, c {} => {}".format(a, b, c, _result))
    return _result


@celery_app.task(bind=True)
@celery_task_logger
@simple_log
def demo_func(self, a: float, b: float) -> float:
    time.sleep(1)
    _result = a * 2 + b * b
    print("demo_func: a {}, b {} => {}".format(a, b, _result))
    return _result
