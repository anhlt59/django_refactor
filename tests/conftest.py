import pytest

from app.share_resources.event.models import Event
from app.share_resources.master_data.models import *
from app.share_resources.users.models import Admin, Company
from app.site_company.manuscript.models import *
from app.site_student.student_profile.models import *
from app.utils.datetime import get_current_date, get_current_time


@pytest.fixture
def create_event():
    event = Event.objects.create(
        target_year=2022,
        class_division="class division",
        event_name="event",
        pdf_name="pdf name",
        image=settings.DEFAULT_STUDENT_AVT,
        date=get_current_date(),
        start_time=get_current_time().time(),
        end_time=get_current_time().time(),
        place="place",
        place_google="place google",
        stamp="stamp",
        reserve_start=get_current_date(),
        reserve_end=get_current_date(),
        release_url="release_url",
        release_date=get_current_date(),
        publication_end=get_current_date(),
    )
    return event


@pytest.fixture
def create_company_type_category():
    category = CompanyTypeCategory.objects.create(name="category name")
    return category


@pytest.fixture
def create_company_type_master(create_company_type_category):
    category = create_company_type_category
    company_type = CompanyTypeMaster.objects.create(
        name="company type", category=category
    )
    return company_type


@pytest.fixture
def create_work_place_category():
    work_place_category = WorkPlaceCategory.objects.create(
        name="work place category name"
    )
    return work_place_category


@pytest.fixture
def create_work_place_master(create_work_place_category):
    work_place = WorkPlaceMaster.objects.create(
        name="work place name", category=create_work_place_category
    )
    return work_place


@pytest.fixture
def create_job_type_category():
    category = JobTypeCategory.objects.create(name="job category name")
    return category


@pytest.fixture
def create_job_type_master(create_job_type_category):
    job_type = JobTypeMaster.objects.create(
        name="job type", category=create_job_type_category, order_by=1
    )
    return job_type


@pytest.fixture
def create_school_info_master():
    school_info = SchoolInfoMaster.objects.create(
        school_division="division",
        name="name",
        kana="kana",
        college="college",
        department="department",
        bunri="bunri",
        bunri_option="bunri option",
        department_code=123,
        campus="campus",
        prefecture="prefecture",
        city="city",
        local_code="local code",
        establishment_division="establishment division",
        postal_code="code",
        address="address",
        tel="0987654321",
        fax="fax",
        k_code="k code",
        course="course",
        note="note",
        join_research="Join research",
        belong_university="belong university",
        belong_college="belong college",
    )
    return school_info


@pytest.fixture
def create_media():
    media = Media.objects.create(name="name")
    return media


@pytest.fixture
def create_plan():
    plan = Plan.objects.create(name="name", val=1)
    return plan


@pytest.fixture
def create_type_auto_reply_message():
    type_auto_reply_message = TypeAutoReplyMessage.objects.create(name="message type")
    return type_auto_reply_message


@pytest.fixture
def create_student():
    student = Student.objects.create_user(
        email="student@gmail.com", password="password"
    )
    return student


@pytest.fixture
def create_company():
    student = Company.objects.create_user(
        email="company@gmail.com", password="password", type=2
    )
    return student


@pytest.fixture
def create_admin():
    admin = Admin.objects.create_user(
        email="admin@gmail.com", password="password", type=3
    )
    return admin


@pytest.fixture
def create_company_profile(create_company, create_plan):
    company_profile = CompanyProfile.objects.create(
        user=create_company,
        name="name",
        kigyo_kana="kigyo kana",
        kigyo_name="kigyo name",
        main_mail="mail@email.com",
        main_tel="0987654321",
        address="address",
        adopt_status=1,
        notify_mail1="notify1@email.com",
        notify_mail2="notify2@gmail.com",
        notify_mail3="notify3@email.com",
        plan=create_plan,
    )
    return company_profile


@pytest.fixture
def create_manuscript(create_student, create_company_profile, create_plan):
    manuscript = Manuscript.objects.create(
        type=1,
        year=2020,
        order=1,
        company_description="company description",
        reported=1,
        accept_entry_flg=1,
        auto_follow_flg=1,
        display_new_flg=1,
        mail_dm_flg=1,
        push_feed_flg=1,
        personal_message_flg=1,
        production_of_job_drafts_feed=1,
        auto_reply_message_ctm=1,
        mail_dm_count=1,
        manuscript_plan_type=1,
        publish_status=1,
        press_status=1,
        assign_status=1,
        manuscript_status=1,
        recruitment_status=1,
        assign_writer=1,
        creative_agency=1,
        push_feed_count=1,
        mail_dm_count_reality=1,
        push_feed_count_reality=1,
        display_recommended_count=1,
        pickup_count=1,
        publication_start_date=get_current_time(),
        publication_end_date=get_current_time(),
        created_by=create_student,
        updated_by=create_student,
        company=create_company_profile,
        plan=create_plan,
    )
    return manuscript
