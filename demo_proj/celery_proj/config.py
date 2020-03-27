from kombu import Queue

from celery_proj.basic_config import *

assert BROKER_URL is not None

# 队列名称
QUEUE_A = "Q-A"
QUEUE_B = "Q-B"
QUEUE_C = "Q-C"

# default queue
CELERY_TASK_DEFAULT_QUEUE = QUEUE_A
CELERY_TASK_CREATE_MISSING_QUEUES = True

CELERY_QUEUES = (
    Queue(name=QUEUE_A, exchange=QUEUE_A, routing_key=QUEUE_A),
    Queue(name=QUEUE_B, exchange=QUEUE_B, routing_key=QUEUE_B),
    Queue(name=QUEUE_C, exchange=QUEUE_C, routing_key=QUEUE_C),
)

CELERY_ROUTES = {
    'celery_proj.tasks.simple_math.demo_sum': {"queue": QUEUE_A},
    'celery_proj.tasks.simple_math.demo_func': {"queue": QUEUE_B},
    'celery_proj.tasks.timeout_task.timeout_task': {"queue": QUEUE_C},
}

# include all task
CELERY_IMPORTS = (
    "celery_proj.tasks",
    "celery_proj.tasks.simple_math",
    "celery_proj.tasks.timeout_task",
)
