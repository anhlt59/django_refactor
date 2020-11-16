from django.db import models

from ..company_profile.models import CompanyProfile
from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin
from ...share_resources.master_data.models import TypeAutoReplyMessage
from ...utils.storages import MediaRootS3Boto3Storage


class Message(TimeStampMixin):
    body = models.TextField(max_length=3000, blank=True, null=True)
    file = models.FileField(storage=MediaRootS3Boto3Storage, blank=True, null=True)

    class Meta:
        db_table = "message"


class MessageTemplate(TimeStampMixin):
    is_master_company = PositiveTinyIntegerField(null=True)
    is_master_student = PositiveTinyIntegerField(null=True)
    is_company = PositiveTinyIntegerField(null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    body = models.TextField(max_length=3000, blank=True, null=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "message_template"


class AutoReplyMessage(TimeStampMixin):
    template_name = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = PositiveTinyIntegerField()
    type_auto_reply_message = models.ForeignKey(TypeAutoReplyMessage, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "auto_reply_message"
