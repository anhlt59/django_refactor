from django.core.cache import cache
from django.contrib.auth import get_user_model
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from django_celery.utils import datetime


User = get_user_model()


@celery_app.task()
def get_users_count():
    return User.objects.count()


@periodic_task(
    run_every=(crontab(minute='*/10')),
    ignore_result=True # if True, result will be saved on RESULT_BACKEND
)
def update_users_count():
    total = User.objects.count()
    cache.set('user_count', total)
