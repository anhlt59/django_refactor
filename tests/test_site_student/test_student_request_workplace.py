import pytest

from app.site_student.student_profile.models import *


# test student request workplace
@pytest.mark.django_db
class TestStudentRequestWorkplace:
    def test_student_request_workplace_create(self, create_student_request_workplace):
        assert StudentRequestWorkplace.objects.count() == 1

    def test_student_request_workplace_update(self, create_student_request_workplace, update_student):
        student_request_workplace = create_student_request_workplace
        student_request_workplace.student = update_student
        student_request_workplace.save()

        student_request_workplace_test = StudentRequestWorkplace.objects.get(
            id=student_request_workplace.id)
        assert student_request_workplace_test.student == update_student

    def test_student_request_workplace_delete(self, create_student_request_workplace):
        assert StudentRequestWorkplace.objects.count() == 1
        create_student_request_workplace.delete()
        assert StudentRequestWorkplace.objects.count() == 0
