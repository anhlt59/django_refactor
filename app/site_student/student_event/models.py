from django.conf import settings
from django.db import models

from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin
from ...share_resources.users.models import Student
from ...share_resources.event.models import Event


class Media(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'media'


class EventStudent(TimeStampMixin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    media = models.CharField(max_length=100)
    student_join_status = models.IntegerField(default=1)
    qr_code = models.TextField(blank=True, null=True)

    date_join = models.DateTimeField(blank=True, null=True)
    number_of_date = models.IntegerField(blank=True, null=True)

    status_visit = PositiveTinyIntegerField(default=0)
    status_booked = PositiveTinyIntegerField(default=1)
    status_entries = PositiveTinyIntegerField(default=0)
    updated_status_visit = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'event_students'


class EventStudentStatus(TimeStampMixin):
    status = PositiveTinyIntegerField(default=1)
    date_join = PositiveTinyIntegerField()
    event_student_id = models.IntegerField(blank=True, null=True)
    event_exit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'event_student_status'
