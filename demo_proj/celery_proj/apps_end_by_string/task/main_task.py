# coding:utf-8
__author__ = 'rk.feng'

import time

from celery_proj.apps_end_by_string.priority_app import app

print("[import celery_proj.apps_end_by_string.priority_app.task.main_task]")


@app.task
def main_task(name: str):
    begin_time = time.time()
    print("get task: name {}, get time {}".format(name, begin_time))
    time.sleep(5)
    return name, begin_time
