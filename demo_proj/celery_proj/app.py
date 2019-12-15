# coding:utf-8
__author__ = 'rk.feng'

from celery import Celery

APP_NAME = 'celery-project'

celery_app = Celery(APP_NAME)
celery_app.config_from_object('celery_proj.config')
