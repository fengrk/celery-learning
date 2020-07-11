# coding:utf-8

from celery import Celery
from kombu import Queue

app_name = "redis-priority"
app = Celery(app_name)

app.conf.result_backend = app.conf.broker_url = "redis://redis-stream:6379/1"

app.conf.imports = (
    "celery_proj.apps_end_by_string.task.main_task",
)
app.conf.task_default_queue = "main-queue"

app.conf.task_create_missing_queues = True

app.conf.broker_transport_options = {"queue_order_strategy": "sorted"}

app.conf.worker_prefetch_multiplier = 1

app.conf.task_inherit_parent_priority = True

# 尝试设置两个优先级
app.conf.task_default_priority = 1
app.conf.broker_transport_options = {
    'priority_steps': [0, 1],
}

app.conf.task_queues = (
    Queue("main-queue"),
)

task_routes = {
    'celery_proj.apps_end_by_string.task.main_task.main_task': {
        'queue': 'main-queue',
        'routing_key': 'main-queue.priority',
    },
}

app.conf.task_routes = task_routes
