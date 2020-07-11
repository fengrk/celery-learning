# coding:utf-8
__author__ = 'rk.feng'

import functools
import time


def demo_add(a: float, b: float) -> float:
    return a + b


def simple_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        time_start = time.time()
        try:
            result = func(*args, **kw)
            print('call {}, time_cost {:.2f}, success True'.format(func.__name__, time.time() - time_start))
            return result
        except:
            print('call {}, time_cost {:.2f}, success False'.format(func.__name__, time.time() - time_start))
            raise

    return wrapper


def celery_task_logger(func):
    """计算时间"""

    @functools.wraps(func)
    def wrapper(*args, **kw):
        _time_start = time.time()
        task_id = args[0].request.id
        try:
            print("[task {}]task start!".format(task_id))
        except Exception as e:
            print(e)
        result = func(*args, **kw)
        _time_cost = time.time() - _time_start
        if _time_cost > 1:
            try:
                print("[task {}]task finished! Time cost {:.2f}s".format(task_id, _time_cost))
            except Exception as e:
                print(e)
        return result

    return wrapper
