# Employee fixtures
# @pytest.fixture
# def create_employee():
#     employee = Employee.objects.create(
#         user
#     )
#     return employee


# Config Push fixture
import pytest

from app.site_admin.admin_profile.models import (
    ConfigPush,
    EventCompany,
    EventCompanyField,
    EventCompanyStudent,
    EventDataFree,
    MailMagazine,
    MailMagazineReceiver,
)
from app.utils.datetime import get_current_date, get_current_time


@pytest.fixture
def create_config_push(create_event):
    config_push = ConfigPush.objects.create(
        title="title",
        body="body",
        date=get_current_date(),
        time=get_current_time().time(),
        graduation_year=2016,
        sex="male",
        literary_class="high",
        living_area="Mars",
        extracurricular="extra",
        event_day="2025-10=10",
        event_reservation_status="good",
        event_attendance_status="many",
        department="Finance",
        school_division="Banking",
        event=create_event,
    )
    return config_push


# No need to test

# @pytest.fixture
# def create_config_push_company_type(create_config_push, create_company_type_master):
#     config_push_company_type = ConfigPushCompanyType.objects.create(
#         company_type_master=create_company_type_master,
#         config_push=create_config_push
#     )
#     return config_push_company_type
#
#
# @pytest.fixture
# def create_config_push_job_type(create_config_push, create_job_type_master):
#     config_push_job_type = ConfigPushJobType.objects.create(
#         config_push=create_config_push,
#         job_type_master=create_job_type_master
#     )
#     return config_push_job_type
#
#
# @pytest.fixture
# def create_config_push_work_place(create_config_push, create_work_place_master, ):
#     config_push_work_place = ConfigPushWorkPlace.objects.create(
#         config_push=create_config_push
#     )
#     return config_push_work_place


# Event Company fixtures
@pytest.fixture
def create_event_company(create_event, create_company):
    event_company = EventCompany.objects.create(
        event=create_event,
        company=create_company,
        date_join=get_current_date(),
        store_code=23,
        created_at=get_current_time(),
        company_join_status=3,
        number_join_status=4,
        plan_date=4,
        company_name="Company 1",
        phonetic="lulu",
        catch_copy="eataw",
        job_category="type 1",
        contact="japan",
        job_information="no idea",
        literature="tawet",
        edu_background="high",
        empl_location="hiroshima",
        school_completion_status="done",
        participation_schedule="yes",
        booth_signboard="yeah",
    )
    return event_company


@pytest.fixture
def create_event_data_free(create_event_company):
    event_data_free = EventDataFree.objects.create(
        name="name",
        memo="memo",
        event_company_profile=2,
        event_company=create_event_company,
        corporate_intelligence="corporate intel",
        business_content="model 1",
    )
    return event_data_free


@pytest.fixture
def create_event_company_field(create_event_company):
    event_company_field = EventCompanyField.objects.create(
        event_company=create_event_company,
        field_name="field name",
        field_value="213",
    )
    return event_company_field


@pytest.fixture
def create_event_company_student(create_event_company, create_student):
    event_company_student = EventCompanyStudent.objects.create(
        event_company=create_event_company,
        student=create_student,
        date_join=get_current_time(),
        status=1,
    )
    return event_company_student


# Mail Magazine fixtures
@pytest.fixture
def create_mailmagazine(create_company_profile, create_manuscript):
    mail_magazine = MailMagazine.objects.create(
        sender_id=1,
        type="type",
        subject="math",
        body="body",
        status="status",
        division="division",
        test_mail1="abc",
        test_mail2="abc",
        test_mail3="abc",
        test_mail4="abdc",
        filter_event="tea",
        filter_bunri="twaeuiht",
        filter_department_division="wte",
        filter_school="wfa",
        filter_prefecture="gawge",
        filter_sex="female",
        filter_club_activities="active",
        receivers=12,
        campaign_id="comp1",
        segment_id="twa",
        mail_open_rate="1.123",
        messages_delivered=12,
        messages_opened=41,
        company=create_company_profile,
        manuscript=create_manuscript,
    )
    return mail_magazine


@pytest.fixture
def create_mail_magazine_receiver(create_mailmagazine, create_student):
    mail_magazine_receiver = MailMagazineReceiver.objects.create(
        student=create_student,
        content="receiver",
        mail_magazine=create_mailmagazine,
    )
    return mail_magazine_receiver
