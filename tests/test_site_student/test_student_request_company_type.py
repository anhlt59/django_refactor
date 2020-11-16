import pytest

from app.site_student.student_profile.models import *


# test student request company type
@pytest.mark.django_db
class TestStudentRequestCompanyType:
    def test_student_request_company_type_create(self, create_student_request_company_type):
        assert StudentRequestCompanyType.objects.count() == 1

    def test_student_request_company_type_update(self, create_student_request_company_type, update_student):
        student_request_company_type = create_student_request_company_type
        student_request_company_type.student = update_student
        student_request_company_type.save()

        student_request_company_type_test = StudentRequestCompanyType.objects.get(
            id=student_request_company_type.id)
        assert student_request_company_type_test.student == update_student

    def test_student_request_company_type_delete(self, create_student_request_company_type):
        assert StudentRequestCompanyType.objects.count() == 1
        create_student_request_company_type.delete()
        assert StudentRequestCompanyType.objects.count() == 0
