import os
from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# current timezone set
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



# CELERY BEAT SCHEDULAR SETTING
app.conf.beat_schedule = {
  'add-every-2-seconds': {
    'task': 'tasks.add',
    'schedule': 2.0,
    'args': (50, 50)
  },
}
