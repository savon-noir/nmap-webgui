from celery import Celery
from nmapui import celeryconfig

celery = Celery()
celery.config_from_object(celeryconfig)
