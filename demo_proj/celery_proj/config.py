from kombu import Queue

# 消息
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_MESSAGE_COMPRESSION = "gzip"
CELERY_TASK_SERIALIZER = "json"
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

CELERY_RESULT_BACKEND = BROKER_URL = "redis://redis-stream:6379/0"

# 队列名称
QUEUE_A = "Q-A"
QUEUE_B = "Q-B"

# default queue
CELERY_TASK_DEFAULT_QUEUE = QUEUE_A
CELERY_TASK_CREATE_MISSING_QUEUES = True

CELERY_QUEUES = (
    Queue(name=QUEUE_A, exchange=QUEUE_A, routing_key=QUEUE_A),
    Queue(name=QUEUE_B, exchange=QUEUE_B, routing_key=QUEUE_B),
)

CELERY_ROUTES = {
    'celery_proj.tasks.simple_math.demo_sum': {"queue": QUEUE_A},
    'celery_proj.tasks.simple_math.demo_func': {"queue": QUEUE_B},
}

# include all task
CELERY_IMPORTS = (
    "celery_proj.tasks",
    "celery_proj.tasks.simple_math",
)
