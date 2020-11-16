import pytest

from app.site_student.student_profile.models import *


# test student request job type
@pytest.mark.django_db
class TestStudentRequestJobType:
    def test_student_request_job_type_create(self, create_student_request_job_type):
        assert StudentRequestJobType.objects.count() == 1

    def test_student_request_job_type_update(self, create_student_request_job_type, update_student):
        student_request_job_type = create_student_request_job_type
        student_request_job_type.student = update_student
        student_request_job_type.save()

        student_request_job_type_test = StudentRequestJobType.objects.get(
            id=student_request_job_type.id)
        assert student_request_job_type_test.student == update_student

    def test_student_request_job_type_delete(self, create_student_request_job_type):
        assert StudentRequestJobType.objects.count() == 1
        create_student_request_job_type.delete()
        assert StudentRequestJobType.objects.count() == 0
