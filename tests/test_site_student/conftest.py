from tests.conftest import *


@pytest.fixture
def create_student_profile(create_student, create_media):
    student_profile = StudentProfile.objects.create(student=create_student, media=create_media,
                                                    first_name="first name", last_name="last name",
                                                    first_name_kana="first name kana", last_name_kana="last name kana",
                                                    sex="male", image=settings.DEFAULT_STUDENT_AVT, bunri="bunri",
                                                    qr_code="qr code",
                                                    school="school", school_division="division", school_prefix="prefix",
                                                    school_prefecture="prefecture",
                                                    club_activities="club activities", college="college", year=2020,
                                                    graduation_date=get_current_time(),
                                                    after_graduation_service=1, renewal_date_student=get_current_time(),
                                                    renewal_date_master=get_current_time(),
                                                    closed=get_current_time(),
                                                    tel="09895624614", tel_ng=0, note="note",
                                                    contact_postal_code="postal",
                                                    contact_prefecture="contact prefecture",
                                                    contact_city="contact city", contact_town="contact town",
                                                    contact_section="contact section",
                                                    postal_code="postal", prefecture="prefecture", city="city",
                                                    town="town",
                                                    section="section",
                                                    department="department", department_division="department division",
                                                    posting=1,
                                                    accept_mail_flg=1, accept_dm_flg=1, accept_tel_flg=1,
                                                    admin_updated=get_current_time(),
                                                    student_updated=get_current_time(),
                                                    status=1)
    return student_profile


@pytest.fixture
def create_student_request_company_type(create_student, create_company_type_master):
    student_request_company_type = StudentRequestCompanyType.objects.create(student=create_student,
                                                                            company_type_master=create_company_type_master)
    return student_request_company_type


@pytest.fixture
def create_student_request_feature(create_student):
    student_request_feature = StudentRequestFeature.objects.create(name="name", student=create_student)

    return student_request_feature


@pytest.fixture
def create_student_request_job_type(create_student, create_job_type_master):
    student_request_job_type = StudentRequestJobType.objects.create(student=create_student,
                                                                    job_type_master=create_job_type_master)

    return student_request_job_type


@pytest.fixture
def create_student_request_workplace(create_student, create_work_place_master):
    student_request_workplace = StudentRequestWorkplace.objects.create(student=create_student,
                                                                       work_place_master=create_work_place_master)

    return student_request_workplace


@pytest.fixture
def update_student():
    student = Student.objects.create_user(email="student_update@gmail.com", password="password_update")
    return student
