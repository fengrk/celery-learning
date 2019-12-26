# coding:utf-8
__author__ = 'rk.feng'
import random
import time

from celery_proj.tasks.simple_math import demo_sum, demo_func
from celery_proj.tasks.timeout_task import timeout_task

if __name__ == '__main__':
    for i in range(100000):
        demo_sum.delay(a=random.random() * 10, b=random.random() * 2, c=random.random())

        if random.random() > 0.5:
            demo_func.delay(10 * random.random(), random.randint(1, 100))

        timeout_task.delay(random.randint(2, 10))

        time.sleep(0.5)
