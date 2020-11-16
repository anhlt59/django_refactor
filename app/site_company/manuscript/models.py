from django.db import models

from ..company_profile.models import CompanyProfile
from ...core.db.fields import PositiveTinyIntegerField
from ...core.db.models import TimeStampMixin
from ...share_resources.master_data.models import Plan, JobTypeMaster, WorkPlaceMaster
from ...share_resources.users.models import User
from ...utils.storages import MediaRootS3Boto3Storage


class Manuscript(TimeStampMixin):
    type = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    order = models.IntegerField(null=True)
    company_description = models.CharField(max_length=300, blank=True, null=True)
    reported = models.IntegerField(null=True)
    accept_entry_flg = models.IntegerField(null=True)
    auto_follow_flg = models.IntegerField(null=True)
    display_new_flg = models.IntegerField(null=True)
    mail_dm_flg = models.IntegerField(null=True)
    push_feed_flg = models.IntegerField(null=True)
    personal_message_flg = models.IntegerField(null=True)
    production_of_job_drafts_feed = models.IntegerField(null=True)
    auto_reply_message_ctm = models.IntegerField(null=True)
    mail_dm_count = models.IntegerField(null=True)
    manuscript_plan_type = models.IntegerField(null=True)
    publish_status = models.IntegerField(null=True)
    press_status = models.IntegerField(null=True)
    assign_status = models.IntegerField(null=True)
    manuscript_status = models.IntegerField(null=True)
    recruitment_status = models.IntegerField(null=True)
    assign_writer = models.IntegerField(null=True)
    creative_agency = PositiveTinyIntegerField(null=True)
    push_feed_count_reality = models.IntegerField(null=True)
    mail_dm_count_reality = models.IntegerField(null=True)
    push_feed_count = models.IntegerField(null=True)
    display_recommended_count = models.IntegerField(null=True)
    pickup_count = models.IntegerField(null=True)
    publication_start_date = models.DateTimeField(blank=True, null=True)
    publication_end_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="manuscript_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="manuscript_updaters")
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta:
        db_table = "manuscript"


class ManuscriptProfile(TimeStampMixin):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    cover = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    company_name = models.CharField(max_length=300, blank=True, null=True)
    company_name_kana = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    is_coordinate = PositiveTinyIntegerField(default=0)
    map_visibility = models.IntegerField(null=True)
    map_info = models.CharField(max_length=2000, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_updaters")

    class Meta:
        db_table = "manuscript_profile"


class ManuscriptAdoption(TimeStampMixin):
    image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    job_type = models.TextField(blank=True, null=True)
    job_content = models.TextField(blank=True, null=True)
    office_place = models.CharField(max_length=300, blank=True, null=True)
    job_time = models.CharField(max_length=300, blank=True, null=True)
    holiday = models.CharField(max_length=300, blank=True, null=True)
    new_employees_number = models.CharField(max_length=300, blank=True, null=True)
    recruited_school = models.CharField(max_length=1000, blank=True, null=True)
    target_subject = models.CharField(max_length=1000, blank=True, null=True)
    selection_way = models.CharField(max_length=2000, blank=True, null=True)
    selection_process = models.CharField(max_length=300, blank=True, null=True)
    selection_document = models.CharField(max_length=1000, blank=True, null=True)
    salary = models.CharField(max_length=300, blank=True, null=True)
    allowances = models.CharField(max_length=300, blank=True, null=True)
    salary_increase = models.CharField(max_length=300, blank=True, null=True)
    bonus = models.CharField(max_length=300, blank=True, null=True)
    insurance = models.CharField(max_length=300, blank=True, null=True)
    benefit = models.CharField(max_length=300, blank=True, null=True)
    free = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=300, blank=True, null=True)
    manuscript = models.OneToOneField(Manuscript, on_delete=models.CASCADE)
    academic_history = models.CharField(max_length=50, blank=True, null=True)
    faculty = models.CharField(max_length=50, blank=True, null=True)
    free_content = models.TextField(blank=True, null=True)
    title_image = models.CharField(max_length=400, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_adoption_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_adoption_updaters")
    educate_training = models.TextField(blank=True, null=True)
    recruit_retire = models.CharField(max_length=300, blank=True, null=True)
    hiring_per_gender = models.CharField(max_length=300, blank=True, null=True)
    service_years = models.CharField(max_length=300, blank=True, null=True)
    average_ot = models.CharField(max_length=300, blank=True, null=True)
    days_off = models.CharField(max_length=300, blank=True, null=True)
    last_year_child_care_leave = models.CharField(max_length=300, blank=True, null=True)
    women_employee_percent = models.CharField(max_length=300, blank=True, null=True)
    probation = models.CharField(max_length=300, blank=True, null=True)
    free_title = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = "manuscript_adoption"


class ManuscriptAdoptionDataFree(TimeStampMixin):
    name = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    manuscript_adoption = models.ForeignKey(ManuscriptAdoption, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_adoption_data_free_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_adoption_data_free_updaters")

    class Meta:
        db_table = "manuscript_adoption_data_free"


class ManuscriptCompanyData(TimeStampMixin):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    representative = models.CharField(max_length=45, blank=True, null=True)
    establishment_date = models.CharField(max_length=30, blank=True, null=True)
    employee_number = models.CharField(max_length=300, blank=True, null=True)
    capital = models.CharField(max_length=300, blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    headquarters = models.CharField(max_length=1000, blank=True, null=True)
    amount_of_sale = models.CharField(max_length=300, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_udaters")

    class Meta:
        db_table = "manuscript_company_data"


class ManuscriptCompanyDataFree(TimeStampMixin):
    name = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    manuscript_company_data = models.ForeignKey(ManuscriptCompanyData, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_free_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_free_updaters")

    class Meta:
        db_table = "manuscript_company_data_free"


class ManuscriptCompanyDataSite(TimeStampMixin):
    name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    manuscript_company_data = models.ForeignKey(ManuscriptCompanyData, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_site_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_data_site_updaters")

    class Meta:
        db_table = "manuscript_company_data_site"


class ManuscriptStudentRelation(TimeStampMixin):
    # student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.SET_NULL, null=True)
    status_0 = PositiveTinyIntegerField(default=0)
    follow_time = models.DateTimeField(blank=True, null=True)
    status_1 = PositiveTinyIntegerField(default=0)
    status_2 = PositiveTinyIntegerField(default=0)
    status_3 = PositiveTinyIntegerField(default=0)
    status_4 = PositiveTinyIntegerField(default=0)
    status_5 = PositiveTinyIntegerField(default=0)
    status_6 = PositiveTinyIntegerField(default=0)
    status_7 = PositiveTinyIntegerField(default=0)
    status_8 = PositiveTinyIntegerField(default=0)
    entry_time = models.DateTimeField(blank=True, null=True)
    message_flg = PositiveTinyIntegerField(null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.SET_NULL, null=True)
    status_05 = PositiveTinyIntegerField(default=0)
    status_05_created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "manuscript_student_relation"


class ManuscriptProfileFeatureTag(TimeStampMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    manuscript_profile = models.ForeignKey(ManuscriptProfile, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_feature_tag_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_feature_tag_updaters")

    class Meta:
        db_table = "manuscript_profile_feature_tag"


class ManuscriptProfileJobType(TimeStampMixin):
    job_type_master = models.ForeignKey(JobTypeMaster, on_delete=models.CASCADE)
    manuscript_profile = models.ForeignKey(ManuscriptProfile, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_job_type_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_job_type_updaters")

    class Meta:
        db_table = "manuscript_profile_job_type"


class ManuscriptProfileWorkPlace(TimeStampMixin):
    work_place_master = models.ForeignKey(WorkPlaceMaster, on_delete=models.CASCADE)
    manuscript_profile = models.ForeignKey(ManuscriptProfile, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_workplace_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_profile_workplace_updaters")

    class Meta:
        db_table = "manuscript_profile_work_place"


class FeedCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "feed_category"


class Feed(TimeStampMixin):
    title = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    eyecatch_image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    movie = models.CharField(max_length=100, blank=True, null=True)
    feed_category = models.ForeignKey(FeedCategory, on_delete=models.SET_NULL, null=True)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.SET_NULL, null=True)
    recommend = models.IntegerField(null=True)
    status = PositiveTinyIntegerField(default=0)
    views = models.IntegerField(null=True)
    private_status = PositiveTinyIntegerField(default=0)
    is_push_notify = PositiveTinyIntegerField(default=1)

    class Meta:
        db_table = "feed"


class ManuscriptCompanyAppeal(TimeStampMixin):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    climate_image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    feed_1 = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True, related_name="manuscript_company_appeal_feed_1")
    feed_2 = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True, related_name="manuscript_company_appeal_feed_2")
    feed_3 = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True, related_name="manuscript_company_appeal_feed_3")
    feed_4 = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True, related_name="manuscript_company_appeal_feed_4")
    feed_5 = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True, related_name="manuscript_company_appeal_feed_5")
    title_image_1 = models.CharField(max_length=100, blank=True, null=True)
    title_image_2 = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_appeal_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_appeal_updaters")

    class Meta:
        db_table = "manuscript_company_appeal"


class ManuscriptCompanyAppealPoint(TimeStampMixin):
    image = models.ImageField(storage=MediaRootS3Boto3Storage, blank=True, null=True)
    message = models.CharField(max_length=300, blank=True, null=True)
    manuscript_company_appeal = models.ForeignKey(ManuscriptCompanyAppeal, on_delete=models.CASCADE)
    point = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_appeal_point_creators")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   related_name="manuscript_company_appeal_point_updaters")

    class Meta:
        db_table = "manuscript_company_appeal_point"


class FeedCategoryMany(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True)
    feed_category = models.ForeignKey(FeedCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "feed_category_many"


class PickupCompany(models.Model):
    year = models.IntegerField(null=True)
    is_intern = PositiveTinyIntegerField(default=0)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)

    class Meta:
        db_table = "pickuped_company"


class CompanyFeedNotify(TimeStampMixin):
    company = models.ForeignKey(CompanyProfile, on_delete=models.SET_NULL, null=True)
    manuscript = models.ForeignKey(Manuscript, on_delete=models.SET_NULL, null=True)
    feed = models.ForeignKey(Feed, on_delete=models.SET_NULL, null=True)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    status = PositiveTinyIntegerField(null=True)
    uuid = models.UUIDField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "company_feed_notify"
