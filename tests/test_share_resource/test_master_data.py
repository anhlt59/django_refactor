import pytest

from app.share_resources.master_data.models import *


# test company_type_category
@pytest.mark.django_db
class TestCompanyTypeCategory:
    def test_create(self, create_company_type_category):
        assert CompanyTypeCategory.objects.count() == 1

    def test_update(self, create_company_type_category):
        category = create_company_type_category
        category.name = "category name update"
        category.save()

        category_test = CompanyTypeCategory.objects.get(id=category.id)
        assert category_test.name == "category name update"

    def test_delete(self, create_company_type_category):
        assert CompanyTypeCategory.objects.count() == 1
        CompanyTypeCategory.objects.get(id=create_company_type_category.id).delete()
        assert CompanyTypeCategory.objects.count() == 0


# test company_type_master
@pytest.mark.django_db
class TestCompanyTypeMaster:
    def test_create(self, create_company_type_master):
        assert CompanyTypeMaster.objects.count() == 1

    def test_update(self, create_company_type_master):
        company_type = create_company_type_master
        company_type.name = "company type update"
        company_type.save()

        company_type_test = CompanyTypeMaster.objects.get(id=company_type.id)
        assert company_type_test.name == "company type update"

    def test_delete(self, create_company_type_master):
        assert CompanyTypeMaster.objects.count() == 1
        create_company_type_master.delete()
        assert CompanyTypeMaster.objects.count() == 0


# test work_place_category
@pytest.mark.django_db
class TestWorkPlaceCategory:
    def test_create(self, create_work_place_category):
        assert WorkPlaceCategory.objects.count() == 1

    def test_update(self, create_work_place_category):
        work_place_category = create_work_place_category
        work_place_category.name = "work place category name update"
        work_place_category.save()

        work_place_category_test = WorkPlaceCategory.objects.get(id=create_work_place_category.id)
        assert work_place_category_test.name == "work place category name update"

    def test_delete(self, create_work_place_category):
        assert WorkPlaceCategory.objects.count() == 1
        WorkPlaceCategory.objects.get(id=create_work_place_category.id).delete()
        assert WorkPlaceCategory.objects.count() == 0


# test work_place_master
@pytest.mark.django_db
class TestWorkPlaceMaster:
    def test_create(self, create_work_place_master):
        assert WorkPlaceMaster.objects.count() == 1

    def test_update(self, create_work_place_master):
        work_place = create_work_place_master
        work_place.name = "work place name"
        work_place.save()

        work_place_test = WorkPlaceMaster.objects.get(id=work_place.id)
        assert work_place_test.name == "work place name"

    def test_delete(self, create_work_place_master):
        assert WorkPlaceMaster.objects.count() == 1
        create_work_place_master.delete()
        assert WorkPlaceMaster.objects.count() == 0


# test job_type_category
@pytest.mark.django_db
class TestJobTypeCategory:
    def test_create(self, create_job_type_category):
        assert JobTypeCategory.objects.count() == 1

    def test_update(self, create_job_type_category):
        job_type = create_job_type_category
        job_type.name = "job name update"
        job_type.save()

        job_type_test = JobTypeCategory.objects.get(id=job_type.id)
        assert job_type_test.name == "job name update"

    def test_delete(self, create_job_type_category):
        assert JobTypeCategory.objects.count() == 1
        create_job_type_category.delete()
        assert JobTypeCategory.objects.count() == 0


# test job_type_master
@pytest.mark.django_db
class TestJobTypeMaster:
    def test_create(self, create_job_type_master):
        assert JobTypeMaster.objects.count() == 1

    def test_update(self, create_job_type_master):
        job_type = create_job_type_master
        job_type.name = "job type update"
        job_type.save()

        job_type_test = JobTypeMaster.objects.get(id=job_type.id)
        assert job_type_test.name == "job type update"

    def test_delete(self, create_job_type_master):
        assert JobTypeMaster.objects.count() == 1
        create_job_type_master.delete()
        assert JobTypeMaster.objects.count() == 0


# test school_info_master
@pytest.mark.django_db
class TestSchoolInfoMaster:
    def test_create(self, create_school_info_master):
        assert SchoolInfoMaster.objects.count() == 1

    def test_update(self, create_school_info_master):
        school_info = create_school_info_master
        school_info.name = "name update"
        school_info.save()

        school_info_test = SchoolInfoMaster.objects.get(id=school_info.id)
        assert school_info_test.name == "name update"

    def test_delete(self, create_school_info_master):
        assert SchoolInfoMaster.objects.count() == 1
        create_school_info_master.delete()
        assert SchoolInfoMaster.objects.count() == 0


# test media
@pytest.mark.django_db
class TestMedia:
    def test_create(self, create_media):
        assert Media.objects.count() == 1

    def test_update(self, create_media):
        media = create_media
        media.name = "name update"
        media.save()

        media_update = Media.objects.get(id=media.id)
        assert media_update.name == "name update"

    def test_delete(self, create_media):
        assert Media.objects.count() == 1
        create_media.delete()
        assert Media.objects.count() == 0


# test Plan
@pytest.mark.django_db
class TestPlan:
    def test_create(self, create_plan):
        assert Plan.objects.count() == 1

    def test_update(self, create_plan):
        plan = create_plan
        plan.name = "name update"
        plan.save()

        plan_test = Plan.objects.get(id=plan.id)
        assert plan_test.name == "name update"

    def test_delete(self, create_plan):
        assert Plan.objects.count() == 1
        create_plan.delete()
        assert Plan.objects.count() == 0


# test type_auto_reply_message
@pytest.mark.django_db
class TestTypeAutoReplyMessage:
    def test_create(self, create_type_auto_reply_message):
        assert TypeAutoReplyMessage.objects.count() == 1

    def test_update(self, create_type_auto_reply_message):
        type_auto_reply_message = create_type_auto_reply_message
        type_auto_reply_message.name = "type update"
        type_auto_reply_message.save()

        type_auto_reply_message_test = TypeAutoReplyMessage.objects.get(id=type_auto_reply_message.id)
        assert type_auto_reply_message_test.name == "type update"

    def test_delete(self, create_type_auto_reply_message):
        assert TypeAutoReplyMessage.objects.count() == 1
        create_type_auto_reply_message.delete()
        assert TypeAutoReplyMessage.objects.count() == 0
