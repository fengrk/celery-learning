# coding:utf-8

from time import sleep

from celery import Celery
from kombu import Queue

app_name = "redis-priority"
app = Celery(app_name)

app.conf.result_backend = app.conf.broker_url = "redis://redis-stream:6379/1"

app.conf.task_default_queue = "b-medium"

app.conf.task_create_missing_queues = True

# app.conf.task_default_priority = 3

app.conf.broker_transport_options = {"queue_order_strategy": "sorted"}

app.conf.worker_prefetch_multiplier = 1

app.conf.task_inherit_parent_priority = True

# app.conf.broker_transport_options = {
#    'priority_steps': list(range(10)),
# }

app.conf.task_queues = (
    Queue("a-high"),
    Queue("b-medium"),
    Queue("c-low"),
)

app.conf.task_routes = {
    'celery_proj.other_apps.redis_priority.low_priority_wait': {
        'queue': 'c-low',
        'routing_key': 'c-low.priority',
    },
    'celery_proj.other_apps.redis_priority.high_priority_wait': {
        'queue': 'a-high',
        'routing_key': 'a-high.priority',
    },
}

sleep_seconds = 0.1


def _wait(*args, **kwargs):
    if not kwargs:
        for a in args:
            if type(a) is dict:
                kwargs = a
    print(kwargs.get("fixture_name"))
    sleep(sleep_seconds)
    return kwargs.get("fixture_name", "UNKNOWN")


@app.task
def wait(*args, **kwargs):
    return _wait(*args, **kwargs)


@app.task
def low_priority_wait(*args, **kwargs):
    return _wait(*args, **kwargs)


@app.task
def high_priority_wait(*args, **kwargs):
    return _wait(*args, **kwargs)
