from django.db import models

from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import PolicyMixin
from ...utils.storages import MediaRootS3Boto3Storage


class Event(PolicyMixin):
    target_year = models.IntegerField(null=True)
    class_division = models.CharField(max_length=100, blank=True, null=True)
    event_name = models.TextField()
    pdf_name = models.TextField()
    image = models.ImageField(storage=MediaRootS3Boto3Storage)
    date = models.DateField()
    sub_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    sub_start_time = models.TimeField(blank=True, null=True)
    sub_end_time = models.TimeField(blank=True, null=True)
    place = models.TextField()
    place_google = models.TextField()
    sub_place = models.TextField(blank=True, null=True)
    sub_place_google = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    stamp = models.CharField(max_length=10)
    reserve_start = models.DateField()
    reserve_end = models.DateField()
    release_url = models.TextField()
    release_date = models.DateField()
    publication_end = models.DateField()
    is_top_display = PositiveTinyIntegerField(default=0)

    class Meta:
        db_table = "event"
