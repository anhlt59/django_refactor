import pytest

from app.site_admin.admin_profile.models import ConfigPush


# test config_push
@pytest.mark.django_db
class TestConfigPush:
    def test_create(self, create_config_push):
        assert ConfigPush.objects.count() == 1

    def test_update(self, create_config_push):
        config_push = create_config_push
        config_push.title = "title update"
        config_push.save()

        config_push_test = ConfigPush.objects.get(id=config_push.id)
        assert config_push_test.title == "title update"

    def test_delete(self, create_config_push):
        assert ConfigPush.objects.count() == 1
        create_config_push.delete()
        assert ConfigPush.objects.count() == 0


# No need to test

# @pytest.mark.django_db
# class TestConfigPushCompanyType:
#     def test_create(self, create_config_push_company_type):
#         assert ConfigPushCompanyType.objects.count() == 1
#
#     def test_update(self, create_config_push_company_type):
#         config_push_company_type = create_config_push_company_type
#         config_push_company_type.config_push_id = 1
#         config_push_company_type.save()
#         config_push_company_type.test = ConfigPushCompanyType.objects.get(id=config_push_company_type.id)
#         assert config_push_company_type.test.config_push_id == 1
#
#     def test_delete(self, create_config_push_company_type):
#         assert ConfigPushCompanyType.objects.count() == 1
#         create_config_push_company_type.delete()
#         assert ConfigPushCompanyType.objects.count() == 0
#
#
# @pytest.mark.django_db
# class TestConfigPushJobType:
#     def test_create(self, create_config_push_job_type):
#         assert ConfigPushJobType.objects.count() == 1
#
#     def test_update(self, create_config_push_job_type):
#         config_push_job_type = create_config_push_job_type
#         config_push_job_type.config_push_id = 1
#         config_push_job_type.save()
#         config_push_job_type_test = ConfigPushWorkPlace.objects.get(id=config_push_job_type.id)
#         assert config_push_job_type_test.config_push_id == 1
#
#     def test_delete(self, create_config_push_job_type):
#         assert ConfigPushJobType.objects.count() == 1
#         create_config_push_job_type.delete()
#         assert ConfigPushJobType.objects.count() == 0
#
#
# @pytest.mark.django_db
# class TestConfigPushWorkPlace:
#     def test_create(self, create_config_push_work_place):
#         assert ConfigPushWorkPlace.objects.count() == 1
#
#     def test_update(self, create_config_push_work_place):
#         config_push_work_place = create_config_push_work_place
#         config_push_work_place.config_push_id = 1
#         config_push_work_place.save()
#         config_push_work_place_test = ConfigPushWorkPlace.objects.get(id=config_push_work_place.id)
#         assert config_push_work_place_test.config_push_id == 1
#
#     def test_delete(self, create_config_push_work_place):
#         assert ConfigPushWorkPlace.objects.count() == 1
#         create_config_push_work_place.delete()
#         assert ConfigPushWorkPlace.objects.count() == 0
