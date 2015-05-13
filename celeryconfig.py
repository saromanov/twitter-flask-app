import os
import sys

sys.path.insert(0, os.getcwd())

BROKER_URL = 'redis://localhost:6379'
CELERY_BACKEND='redis'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ENABLE_UTC = True
CELERYD_CONCURRENCY = 10
CELERYD_TASK_TIME_LIMIT = 60
CELERY_ANNOTATIONS = {'tasks.getTweetsByWords': {'rate_limit': '100/s'}}
