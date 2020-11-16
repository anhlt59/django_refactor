import pytest

from app.site_student.student_profile.models import *


# test student request feature
@pytest.mark.django_db
class TestStudentRequestFeature:
    def test_student_request_feature_create(self, create_student_request_feature):
        assert StudentRequestFeature.objects.count() == 1

    def test_student_request_feature_update(self, create_student_request_feature):
        student_request_feature = create_student_request_feature
        student_request_feature.name = "name update"
        student_request_feature.save()

        student_request_feature_test = StudentRequestFeature.objects.get(id=student_request_feature.id)
        assert student_request_feature_test.name == "name update"

    def test_student_request_feature_delete(self, create_student_request_feature):
        assert StudentRequestFeature.objects.count() == 1
        create_student_request_feature.delete()
        assert StudentRequestFeature.objects.count() == 0

