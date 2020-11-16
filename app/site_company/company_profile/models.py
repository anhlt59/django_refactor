from django.db import models

from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin
from ...share_resources.master_data.models import Plan
from ...share_resources.users.models import Company
from ...utils.storages import MediaRootS3Boto3Storage


class CompanyProfile(TimeStampMixin):
    user = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True, null=True)
    kigyo_name = models.CharField(max_length=200)
    kigyo_kana = models.CharField(max_length=200)
    main_mail = models.EmailField(max_length=60)
    main_tel = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    adopt_status = PositiveTinyIntegerField(default=0)

    notify_mail1 = models.EmailField(max_length=60, blank=True, null=True)
    notify_mail2 = models.EmailField(max_length=60, blank=True, null=True)
    notify_mail3 = models.EmailField(max_length=60, blank=True, null=True)

    # writer_id = models.ForeignKey(Employee)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta:
        db_table = "company_profile"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, kigyo_name={self.kigyo_name!r})"

    def get_absolute_url(self):
        pass


class SpecialFeature(models.Model):
    year = models.IntegerField(null=True)
    type = PositiveTinyIntegerField(null=True)
    for_event_flg = models.IntegerField(null=True)
    image = models.ImageField(storage=MediaRootS3Boto3Storage)
    title = models.CharField(max_length=300, blank=True, null=True)
    outline = models.CharField(max_length=500, blank=True, null=True)
    publication_start_date = models.DateTimeField(blank=True, null=True)
    publication_end_date = models.DateTimeField(blank=True, null=True)
    status = PositiveTinyIntegerField(null=True)
    pv_count = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "special_feature"
