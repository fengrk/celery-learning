# 消息
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_MESSAGE_COMPRESSION = "gzip"
CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_BACKEND = BROKER_URL = "redis://redis-stream:6379/0"

# 队列名称
QUEUE_A = "Q-A"
QUEUE_B = "Q-B"

CELERY_QUEUES = {
    QUEUE_A: {"routing_key": QUEUE_A, "exchange": QUEUE_A},
    QUEUE_B: {"routing_key": QUEUE_B, "exchange": QUEUE_B},
}

# 这个比较重要，和上面的任务队列必须匹配使用，用来把任务队列配到相应函数上
CELERY_ROUTES = {
    'celery_proj.tasks.simple_math.demo_sum': {"routing_key": QUEUE_A, "queue": QUEUE_A},
    'celery_proj.tasks.simple_math.demo_func': {"routing_key": QUEUE_B, "queue": QUEUE_B},
}

# include all task
CELERY_IMPORTS = (
    "celery_proj.tasks",
    "celery_proj.tasks.simple_math",
)
