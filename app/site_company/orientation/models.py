from django.db import models

from ..manuscript.models import Manuscript, ManuscriptStudentRelation
from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin
# from ...site_student.student_profile.models import StudentProfile
from ...utils.storages import MediaRootS3Boto3Storage


class Orientation(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(storage=MediaRootS3Boto3Storage)
    publication_start_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    needs = models.TextField(blank=True, null=True)
    outline = models.TextField(blank=True, null=True)
    free_title_1 = models.TextField(blank=True, null=True)
    free_content_1 = models.TextField(blank=True, null=True)
    free_title_2 = models.TextField(blank=True, null=True)
    free_content_2 = models.TextField(blank=True, null=True)
    number_of_date = models.IntegerField(null=True)

    class Meta:
        db_table = "orientation"


class OrientationPlan(models.Model):
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    reserve_start_date = models.DateField(blank=True, null=True)
    reserve_end_date = models.DateField(blank=True, null=True)
    map_info = models.CharField(max_length=45, blank=True, null=True)
    place = models.CharField(max_length=45, blank=True, null=True)
    is_address = PositiveTinyIntegerField(default=0)
    is_accept_reservation = PositiveTinyIntegerField(default=0)

    class Meta:
        db_table = "orientation_plan"


class ReservedOrientation(TimeStampMixin):
    # student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    datetime_no = PositiveTinyIntegerField(null=True)
    status = models.SmallIntegerField(null=True)
    number_of_day = models.IntegerField(null=True)
    manuscript_student_relation = models.ForeignKey(ManuscriptStudentRelation, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "reserved_orientation"
