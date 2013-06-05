#!/usr/bin/env python
from celery import Celery, task, current_task
from nmapui import celeryconfig
from libnmap.process import NmapProcess

#celery = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp://guest@localhost//')
celery = Celery()
celery.config_from_object(celeryconfig)

@task(name='tasks.nmap_scan')
def celery_nmap_scan(targets, options):
    def status_callback(nmapscan=None, data=''):
        current_task.update_state(state='PROGRESS', meta={
                                               'done': nmapscan.progress,
                                               'etc': nmapscan.etc,
                                               })
    nm = NmapProcess(targets, options, event_callback=status_callback)
    rc = nm.run()

    if rc == 0 and nm.stdout:
        r = nm.stdout
    else:
        r = None

    return {'rc': rc, 'report': r}
