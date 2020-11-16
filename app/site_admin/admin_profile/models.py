# from django.db import models
from app.share_resources.event.models import *
from app.share_resources.master_data.models import *
from app.share_resources.users.models import *
from app.site_company.manuscript.models import *

from ...core.db.fields import *
from ...core.db.models import *


# Employee:
class StaffAuth(models.Model):
    auth = models.CharField(max_length=10)


class Employee(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.PROTECT)
    role = models.ForeignKey(StaffAuth, on_delete=models.PROTECT, null=True)
    login = models.TextField(blank=True)


# Config push
class ConfigPush(TimeStampMixin):
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    graduation_year = models.CharField(max_length=200)
    sex = models.CharField(max_length=100)
    literary_class = models.CharField(max_length=100)
    living_area = models.TextField(blank=True)
    extracurricular = models.CharField(max_length=300)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_day = models.CharField(max_length=200)
    event_reservation_status = models.CharField(max_length=200)
    event_attendance_status = models.CharField(max_length=200)
    department = models.TextField(blank=True)
    school_division = models.TextField(blank=True)
    status = TinyIntegerField(null=True)
    # created_at = models.DateTimeField(null=True)


class ConfigPushCompanyType(models.Model):
    company_type_master = models.ForeignKey(CompanyTypeMaster, on_delete=models.PROTECT)
    config_push = models.ForeignKey(ConfigPush, on_delete=models.CASCADE)


class ConfigPushJobType(models.Model):
    job_type_master = models.ForeignKey(JobTypeMaster, on_delete=models.PROTECT)
    config_push = models.ForeignKey(ConfigPush, on_delete=models.CASCADE)


class ConfigPushWorkPlace(models.Model):
    config_push = models.ForeignKey(ConfigPush, on_delete=models.CASCADE)
    work_place_master = models.ForeignKey(WorkPlaceMaster, on_delete=models.PROTECT)


# Mail magazine models
class MailMagazine(TimeStampMixin):
    sender_id = models.IntegerField(null=True)
    type = models.CharField(max_length=20, default=0)
    subject = models.CharField(max_length=1000)
    body = models.TextField(blank=True)
    sent_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10)
    division = models.CharField(max_length=20)
    reserve_date = models.DateField(blank=True, null=True)
    test_mail1 = models.CharField(max_length=255)
    test_mail2 = models.CharField(max_length=255)
    test_mail3 = models.CharField(max_length=255)
    test_mail4 = models.CharField(max_length=255)
    filter_event = models.CharField(max_length=100)
    filter_bunri = models.CharField(max_length=45)
    filter_department_division = models.CharField(max_length=100)
    filter_school = models.CharField(max_length=45)
    filter_prefecture = models.CharField(max_length=45)
    filter_sex = models.CharField(max_length=45)
    filter_club_activities = models.CharField(max_length=45)
    receivers = models.IntegerField(null=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.PROTECT)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.PROTECT)
    campaign_id = models.CharField(max_length=255)
    segment_id = models.CharField(max_length=255)
    mail_open_rate = models.FloatField(null=True)
    messages_delivered = models.IntegerField(null=True)
    messages_opened = models.IntegerField(null=True)


class MailMagazineReceiver(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    content = models.CharField(max_length=300)
    mail_magazine = models.ForeignKey(MailMagazine, on_delete=models.DO_NOTHING)


# Company Event
class EventCompany(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date_join = models.DateTimeField(null=True, blank=True)
    store_code = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    company_join_status = models.IntegerField(default=1)
    number_join_status = models.IntegerField(default=0)
    plan_date = models.IntegerField(null=True)
    company_name = models.CharField(max_length=50)
    phonetic = models.CharField(max_length=50)
    catch_copy = models.TextField(blank=True)
    job_category = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    job_information = models.CharField(max_length=50)
    industry_information = models.CharField(max_length=50)
    literature = models.CharField(max_length=50)
    edu_background = models.CharField(max_length=100)
    empl_location = models.CharField(max_length=50)
    school_completion_status = models.CharField(max_length=50)
    participation_schedule = models.CharField(max_length=50)
    booth_signboard = models.CharField(max_length=50)


class EventDataFree(models.Model):
    name = models.TextField(blank=True)
    memo = models.TextField(blank=True)
    event_company_profile = models.IntegerField(null=True)
    event_company = models.ForeignKey(EventCompany, on_delete=models.PROTECT)
    corporate_intelligence = models.CharField(max_length=100)
    business_content = models.CharField(max_length=100)


class EventCompanyField(TimeStampMixin):
    event_company = models.ForeignKey(EventCompany, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=45)
    field_value = models.IntegerField()


class EventCompanyStudent(models.Model):
    event_company = models.ForeignKey(EventCompany, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date_join = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(null=True)


# Special Feature
class SpecialFeature(TimeStampMixin):
    year = models.IntegerField(null=True)
    type = TinyIntegerField(null=True)
    for_event_flg = models.IntegerField(default=0)
    image = models.CharField(max_length=500)
    title = models.CharField(max_length=300)
    outline = models.CharField(max_length=500)
    publication_start_date = models.DateField(null=True, blank=True)
    publication_end_date = models.DateField(null=True, blank=True)
    number_listed_company = models.IntegerField(null=True)
    status = TinyIntegerField(default=0)
    pv_count = models.IntegerField(null=True)
    description = models.TextField(blank=True)


class SpecialFeatureAppealPoint(models.Model):
    special_feature = models.ForeignKey(SpecialFeature, on_delete=models.DO_NOTHING)
    point_1 = models.CharField(max_length=60)
    point_2 = models.CharField(max_length=60)
    point_3 = models.CharField(max_length=60)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    year = models.IntegerField(null=True)
