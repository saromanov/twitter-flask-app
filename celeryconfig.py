import os
import sys

sys.path.insert(0, os.getcwd())

BROKER_URL = 'redis://localhost:6379'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ENABLE_UTC = True
CELERY_IMPORTS = ('celery_fun.tasks', )
CELERYD_CONCURRENCY = 10
CELERYD_TASK_TIME_LIMIT = 1
