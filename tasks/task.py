# coding:utf-8
__author__ = 'rk.feng'

import random
import time

from celery import Celery

app = Celery('task', broker='redis://redis-stream:6379/0', backend='redis://redis-stream:6379/0')


@app.task
def send_mail(email):
    print("send mail to ", email)
    time.sleep(5)
    return "success"


@app.task
def add(x: float, y: float):
    return x + y


if __name__ == '__main__':
    for i in range(100000):
        send_mail.delay("no.{}@gmail.com".format(i))

        if random.random() > 0.5:
            add.delay(10 * random.random(), random.randint(1, 100))

        time.sleep(0.5)
