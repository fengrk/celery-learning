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
