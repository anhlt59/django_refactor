import uuid

import pytest
from django.conf import settings

from app.site_company.company_profile.models import SpecialFeature
from app.site_company.manuscript.models import *
from app.site_company.message.models import AutoReplyMessage, Message, MessageTemplate
from app.site_company.orientation.models import (
    Orientation,
    OrientationPlan,
    ReservedOrientation,
)
from app.utils.datetime import get_current_date, get_current_time


@pytest.fixture
def create_special_feature():
    special_feature = SpecialFeature.objects.create(
        year=2020,
        type=1,
        for_event_flg=1,
        image=settings.DEFAULT_STUDENT_AVT,
        title="title",
        outline="outline",
        publication_start_date=get_current_time(),
        publication_end_date=get_current_time(),
        status=1,
        pv_count=1,
        description="description",
    )
    return special_feature


@pytest.fixture
def create_manuscript_profile(create_manuscript, create_student):
    manuscript_profile = ManuscriptProfile.objects.create(
        manuscript=create_manuscript,
        title="title",
        logo=settings.DEFAULT_STUDENT_AVT,
        cover=settings.DEFAULT_STUDENT_AVT,
        company_name="company name",
        company_name_kana="company name kana",
        description="description",
        location="location",
        is_coordinate=1,
        map_visibility=1,
        map_info="map info",
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_profile


@pytest.fixture
def create_manuscript_adoption(create_student, create_manuscript):
    manuscript_adoption = ManuscriptAdoption.objects.create(
        image=settings.DEFAULT_STUDENT_AVT,
        text="text",
        job_type="job type",
        job_content="job content",
        office_place="office place",
        job_time="job time",
        holiday="holiday",
        new_employees_number="5",
        recruited_school="recruited school",
        target_subject="target subject",
        selection_way="selection way",
        selection_process="selection process",
        selection_document="selection document",
        salary="salary",
        allowances="allowances",
        salary_increase="salary increase",
        bonus="bonus",
        insurance="insurance",
        benefit="benefit",
        free="free",
        contact="contact",
        manuscript=create_manuscript,
        academic_history="academic_history",
        faculty="faculty",
        free_content="free content",
        title_image="title image",
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_adoption


@pytest.fixture
def create_manuscript_adoption_data_free(create_student, create_manuscript_adoption):
    manuscript_adoption_data_free = ManuscriptAdoptionDataFree.objects.create(
        name="name",
        memo="memo",
        manuscript_adoption=create_manuscript_adoption,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_adoption_data_free


@pytest.fixture
def create_manuscript_company_data(create_student, create_manuscript):
    manuscript_company_data = ManuscriptCompanyData.objects.create(
        manuscript=create_manuscript,
        description="description",
        representative="representative",
        establishment_date="establishment data",
        employee_number="1",
        capital="capital",
        office="office",
        headquarters="headquarters",
        amount_of_sale="amount of sale",
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_company_data


@pytest.fixture
def create_manuscript_company_data_free(create_student, create_manuscript_company_data):
    manuscript_company_data_free = ManuscriptCompanyDataFree.objects.create(
        name="name",
        memo="memo",
        manuscript_company_data=create_manuscript_company_data,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_company_data_free


@pytest.fixture
def create_manuscript_company_data_size(create_student, create_manuscript_company_data):
    manuscript_company_data_size = ManuscriptCompanyDataSite.objects.create(
        name="name",
        url="url",
        manuscript_company_data=create_manuscript_company_data,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_company_data_size


@pytest.fixture
def create_manuscript_student_relation(create_company_profile, create_manuscript):
    manuscript_student_relation = ManuscriptStudentRelation.objects.create(
        manuscript=create_manuscript,
        status_0=1,
        follow_time=get_current_time(),
        status_1=1,
        status_2=1,
        status_3=1,
        status_4=1,
        status_5=1,
        status_6=1,
        status_05=1,
        status_7=1,
        status_8=1,
        entry_time=get_current_time(),
        message_flg=1,
        remark="remark",
        company=create_company_profile,
        status_05_created_at=get_current_time(),
    )
    return manuscript_student_relation


@pytest.fixture
def create_manuscript_profile_feature_tag(create_manuscript_profile, create_student):
    manuscript_profile_feature_tag = ManuscriptProfileFeatureTag.objects.create(
        name="name",
        manuscript_profile=create_manuscript_profile,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_profile_feature_tag


@pytest.fixture
def create_manuscript_profile_job_type(
    create_job_type_master, create_manuscript_profile, create_student
):
    manuscript_profile_job_type = ManuscriptProfileJobType.objects.create(
        job_type_master=create_job_type_master,
        manuscript_profile=create_manuscript_profile,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_profile_job_type


@pytest.fixture
def create_manuscript_profile_work_place(
    create_work_place_master, create_manuscript_profile, create_student
):
    manuscript_profile_work_place = ManuscriptProfileWorkPlace.objects.create(
        work_place_master=create_work_place_master,
        manuscript_profile=create_manuscript_profile,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_profile_work_place


@pytest.fixture
def create_feed_category():
    feed_category = FeedCategory.objects.create(name="name")
    return feed_category


@pytest.fixture
def create_feed(create_feed_category, create_manuscript):
    feed = Feed.objects.create(
        title="title",
        subject="subject",
        text="text",
        eyecatch_image=settings.DEFAULT_STUDENT_AVT,
        image=settings.DEFAULT_STUDENT_AVT,
        movie="movie",
        feed_category=create_feed_category,
        manuscript=create_manuscript,
        recommend=1,
        views=1,
        private_status=1,
        is_push_notify=1,
    )
    return feed


@pytest.fixture
def create_manuscript_company_appeal(create_manuscript, create_feed, create_student):
    manuscript_company_appeal = ManuscriptCompanyAppeal.objects.create(
        manuscript=create_manuscript,
        image=settings.DEFAULT_STUDENT_AVT,
        message="message",
        climate_image=settings.DEFAULT_STUDENT_AVT,
        feed_1=create_feed,
        feed_2=create_feed,
        feed_3=create_feed,
        feed_4=create_feed,
        feed_5=create_feed,
        title_image_1="title image 1",
        title_image_2="title image 2",
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_company_appeal


@pytest.fixture
def create_manuscript_company_appeal_point(
    create_manuscript_company_appeal, create_student
):
    manuscript_company_appeal_point = ManuscriptCompanyAppealPoint.objects.create(
        image=settings.DEFAULT_STUDENT_AVT,
        message="message",
        manuscript_company_appeal=create_manuscript_company_appeal,
        point=1,
        created_by=create_student,
        updated_by=create_student,
    )
    return manuscript_company_appeal_point


@pytest.fixture
def create_feed_category_many(create_feed, create_feed_category):
    feed_category_many = FeedCategoryMany.objects.create(
        feed_category=create_feed_category, feed=create_feed
    )
    return feed_category_many


@pytest.fixture
def create_pickup_company(create_manuscript):
    pickup_company = PickupCompany.objects.create(
        year=2020, is_intern=1, manuscript=create_manuscript
    )
    return pickup_company


@pytest.fixture
def create_company_feed_notify(create_company_profile, create_manuscript, create_feed):
    company_feed_notify = CompanyFeedNotify.objects.create(
        company=create_company_profile,
        manuscript=create_manuscript,
        feed=create_feed,
        date_start=get_current_date(),
        time_start=get_current_time().time(),
        time_end=get_current_time().time(),
        status=1,
        uuid=uuid.uuid4(),
    )
    return company_feed_notify


@pytest.fixture
def create_message():
    message = Message.objects.create(body="body", file=settings.DEFAULT_STUDENT_AVT)
    return message


@pytest.fixture
def create_message_template(create_company_profile):
    message_template = MessageTemplate.objects.create(
        is_company=1,
        is_master_company=1,
        is_master_student=1,
        name="name",
        body="body",
        company=create_company_profile,
    )
    return message_template


@pytest.fixture
def create_auto_reply_message(create_type_auto_reply_message, create_company_profile):
    auto_reply_message = AutoReplyMessage.objects.create(
        template_name="template name",
        content="content",
        status=1,
        type_auto_reply_message=create_type_auto_reply_message,
        company=create_company_profile,
    )
    return auto_reply_message


@pytest.fixture
def create_orientation(create_manuscript):
    orientation = Orientation.objects.create(
        manuscript=create_manuscript,
        image=settings.DEFAULT_STUDENT_AVT,
        publication_start_date=get_current_time(),
        name="name",
        needs="need",
        outline="outline",
        free_title_1="free title 1",
        free_title_2="free title 2",
        free_content_1="free content 1",
        free_content_2="free content 2",
        number_of_date=1,
    )
    return orientation


@pytest.fixture
def create_orientation_plan(create_orientation):
    orientation_plan = OrientationPlan.objects.create(
        orientation=create_orientation,
        start_date=get_current_date(),
        end_date=get_current_date(),
        start_time=get_current_time().time(),
        end_time=get_current_time().time(),
        reserve_end_date=get_current_date(),
        reserve_start_date=get_current_date(),
        map_info="map info",
        place="place",
        is_address=1,
        is_accept_reservation=1,
    )
    return orientation_plan


@pytest.fixture
def create_reserved_orientation(create_orientation, create_manuscript_student_relation):
    reserved_orientation = ReservedOrientation.objects.create(
        orientation=create_orientation,
        datetime_no=1,
        status=1,
        number_of_day=1,
        manuscript_student_relation=create_manuscript_student_relation,
    )
    return reserved_orientation
