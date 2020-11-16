import pytest

from app.site_student.student_profile.models import *


# test student profile
@pytest.mark.django_db
class TestStudentProfile:
    def test_student_profile_create(self, create_student_profile):
        assert StudentProfile.objects.count() == 1

    def test_student_profile_update(self, create_student_profile):
        student = create_student_profile
        student.first_name = "first name update"
        student.last_name = "last name update"
        student.save()

        student_test = StudentProfile.objects.get(id=student.id)
        assert student_test.first_name == "first name update"
        assert student_test.last_name == "last name update"

    def test_student_profile_delete(self, create_student_profile):
        assert StudentProfile.objects.count() == 1
        create_student_profile.delete()
        assert StudentProfile.objects.count() == 0

