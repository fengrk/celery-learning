# -*- coding: utf-8 -*-

from celery_proj.app import celery_app
from libs.demo_utils import demo_add


@celery_app.task
def demo_sum(a: float, b: float, c: float) -> float:
    _result = demo_add(demo_add(a, b), c)
    print("demo_sum: a {}, b {}, c {} => {}".format(a, b, c, _result))
    return _result


@celery_app.task
def demo_func(a: float, b: float) -> float:
    _result = a * 2 + b * b
    print("demo_func: a {}, b {} => {}".format(a, b, _result))
    return _result
