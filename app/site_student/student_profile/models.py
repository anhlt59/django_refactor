from django.conf import settings
from django.db import models

from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin, PolicyMixin
# from ...site_company.companies.models import CompanyInfo
from ...utils.storages import MediaRootS3Boto3Storage
from ...share_resources.users.models import Student
from ...share_resources.master_data.models import CompanyTypeMaster, JobTypeMaster, WorkPlaceMaster, Media


# student_request_company_type
class StudentRequestCompanyType(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_type_master = models.ForeignKey(CompanyTypeMaster, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_request_company_type'


# student_request_feature
class StudentRequestFeature(models.Model):
    name = models.CharField(max_length=45)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_request_feature'


# student_request_job_type
class StudentRequestJobType(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job_type_master = models.ForeignKey(JobTypeMaster, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_request_job_type'


# student_request_workplace
class StudentRequestWorkplace(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    work_place_master = models.ForeignKey(WorkPlaceMaster, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_request_workplace'


# student
class StudentProfile(TimeStampMixin, PolicyMixin):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="media_student_profile")

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name_kana = models.CharField(max_length=50)
    last_name_kana = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)

    image = models.ImageField(
        storage=MediaRootS3Boto3Storage,
        default=settings.DEFAULT_STUDENT_AVT
    )
    bunri = models.CharField(max_length=5)
    qr_code = models.TextField(blank=True, null=True)

    school = models.CharField(max_length=100, blank=True, null=True)
    school_division = models.CharField(max_length=10)
    school_prefix = models.CharField(max_length=10, blank=True, null=True)
    school_prefecture = models.CharField(max_length=300, blank=True, null=True)
    club_activities = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)

    year = models.IntegerField()
    graduation_date = models.DateTimeField(blank=True, null=True)
    after_graduation_service = PositiveTinyIntegerField(default=1)
    renewal_date_student = models.DateTimeField(blank=True, null=True)
    renewal_date_master = models.DateTimeField(blank=True, null=True)
    closed = models.DateTimeField()

    # contact
    tel = models.CharField(max_length=15)
    tel_ng = models.IntegerField(default=0)
    note = models.TextField(max_length=500)
    contact_postal_code = models.CharField(max_length=10, blank=True)
    contact_prefecture = models.CharField(max_length=45, blank=True)
    contact_city = models.CharField(max_length=100, blank=True)
    contact_town = models.CharField(max_length=100, blank=True)
    contact_section = models.CharField(max_length=200, blank=True)

    # address
    postal_code = models.CharField(max_length=10)
    prefecture = models.CharField(max_length=45)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    section = models.CharField(max_length=200)

    department = models.CharField(max_length=100)
    department_division = models.CharField(max_length=100)
    posting = models.IntegerField(default=1)

    accept_mail_flg = PositiveTinyIntegerField(default=1)
    accept_dm_flg = PositiveTinyIntegerField(default=1)
    accept_tel_flg = models.IntegerField(blank=True, null=True)

    admin_updated = models.DateTimeField(blank=True, null=True)
    student_updated = models.DateTimeField(blank=True, null=True)
    status = PositiveTinyIntegerField(default=1)

    class Meta:
        db_table = 'student_profile'

    def __init__(self, *args, **kwargs):
        super(StudentProfile, self).__init__(*args, **kwargs)

        self.previous_name = f"{self.last_name} {self.first_name}"
        self.previous_image = self.image

    @property
    def current_name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def current_image(self):
        return self.image

    def save(self, *args, **kwargs):
        update_data = {}

        if self.current_name != self.previous_name:
            update_data.update(student_name=self.current_name)
        if self.current_image != self.previous_image:
            update_data.update(image=self.current_image)

        if update_data:
            # update_firebase_document(document, table)
            pass

        super().save(*args, **kwargs)


# duplicate_student
class DuplicateStudent(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'duplicate_student'
