from django.db import models

from app.core.db.models import PolicyMixin


class CompanyTypeCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "company_type_category"


class CompanyTypeMaster(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CompanyTypeCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "company_type_master"


class WorkPlaceCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "work_place_category"


class WorkPlaceMaster(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WorkPlaceCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "work_place_master"


class JobTypeCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "job_type_category"


class JobTypeMaster(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(JobTypeCategory, on_delete=models.CASCADE)
    order_by = models.IntegerField(null=True)

    class Meta:
        db_table = "job_type_master"


class SchoolInfoMaster(PolicyMixin):
    school_division = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    kana = models.CharField(max_length=256, blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    bunri = models.CharField(max_length=10, blank=True, null=True)
    bunri_option = models.CharField(max_length=100, blank=True, null=True)
    department_code = models.IntegerField(null=True)
    campus = models.CharField(max_length=100, blank=True, null=True)
    prefecture = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    local_code = models.CharField(max_length=10, blank=True, null=True)
    establishment_division = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    k_code = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    join_research = models.CharField(max_length=200, blank=True, null=True)
    belong_university = models.CharField(max_length=200, blank=True, null=True)
    belong_college = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "school_info_master"


class Media(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "media"


class Plan(models.Model):
    name = models.CharField(max_length=45)
    val = models.IntegerField()

    class Meta:
        db_table = "plan"


class TypeAutoReplyMessage(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "type_auto_reply_message"
