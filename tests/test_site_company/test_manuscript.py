import pytest

from app.site_company.manuscript.models import *


# test manuscript
@pytest.mark.django_db
class TestManuscript:
    def test_create(self, create_manuscript):
        assert Manuscript.objects.count() == 1

    def test_update(self, create_manuscript):
        manuscript = create_manuscript
        manuscript.year = 2022
        manuscript.save()

        manuscript_test = Manuscript.objects.get(id=manuscript.id)
        assert manuscript_test.year == 2022

    def test_delete(self, create_manuscript):
        assert Manuscript.objects.count() == 1
        create_manuscript.delete()
        assert Manuscript.objects.count() == 0


# test manuscript_profile
@pytest.mark.django_db
class TestManuscriptProfile:
    def test_create(self, create_manuscript_profile):
        assert ManuscriptProfile.objects.count() == 1

    def test_update(self, create_manuscript_profile):
        manuscript_profile = create_manuscript_profile
        manuscript_profile.title = "title update"
        manuscript_profile.save()

        manuscript_profile_test = ManuscriptProfile.objects.get(id=manuscript_profile.id)
        assert manuscript_profile_test.title == "title update"

    def test_delete(self, create_manuscript_profile):
        assert ManuscriptProfile.objects.count() == 1
        create_manuscript_profile.delete()
        assert ManuscriptProfile.objects.count() == 0


# test manuscript_adoption
@pytest.mark.django_db
class TestManuscriptAdoption:
    def test_create(self, create_manuscript_adoption):
        assert ManuscriptAdoption.objects.count() == 1

    def test_update(self, create_manuscript_adoption):
        manuscript_adoption = create_manuscript_adoption
        manuscript_adoption.text = "text update"
        manuscript_adoption.save()

        manuscript_adoption_test = ManuscriptAdoption.objects.get(id=manuscript_adoption.id)
        assert manuscript_adoption_test.text == "text update"

    def test_delete(self, create_manuscript_adoption):
        assert ManuscriptAdoption.objects.count() == 1
        create_manuscript_adoption.delete()
        assert ManuscriptAdoption.objects.count() == 0


# test manuscript_adoption_data_free
@pytest.mark.django_db
class TestManuscriptAdoptionDataFree:
    def test_create(self, create_manuscript_adoption_data_free):
        assert ManuscriptAdoptionDataFree.objects.count() == 1

    def test_update(self, create_manuscript_adoption_data_free):
        manuscript_adoption_data_free = create_manuscript_adoption_data_free
        manuscript_adoption_data_free.name = "name update"
        manuscript_adoption_data_free.save()

        manuscript_adoption_data_free_test = ManuscriptAdoptionDataFree.objects.get(id=manuscript_adoption_data_free.id)
        assert manuscript_adoption_data_free_test.name == "name update"

    def test_delete(self, create_manuscript_adoption_data_free):
        assert ManuscriptAdoptionDataFree.objects.count() == 1
        create_manuscript_adoption_data_free.delete()
        assert ManuscriptAdoptionDataFree.objects.count() == 0


# test manuscript_company_data
@pytest.mark.django_db
class TestManuscriptCompanyData:
    def test_create(self, create_manuscript_company_data):
        assert ManuscriptCompanyData.objects.count() == 1

    def test_update(self, create_manuscript_company_data):
        manuscript_company_data = create_manuscript_company_data
        manuscript_company_data.description = "description update"
        manuscript_company_data.save()

        manuscript_company_data_test = ManuscriptCompanyData.objects.get(id=manuscript_company_data.id)
        assert manuscript_company_data_test.description == "description update"

    def test_delete(self, create_manuscript_company_data):
        assert ManuscriptCompanyData.objects.count() == 1
        create_manuscript_company_data.delete()
        assert ManuscriptCompanyData.objects.count() == 0


# test manuscript_company_data_free
@pytest.mark.django_db
class TestManuscriptCompanyDataFree:
    def test_create(self, create_manuscript_company_data_free):
        assert ManuscriptCompanyDataFree.objects.count() == 1

    def test_update(self, create_manuscript_company_data_free):
        manuscript_company_data_free = create_manuscript_company_data_free
        manuscript_company_data_free.name = "name update"
        manuscript_company_data_free.save()

        manuscript_company_data_free_test = ManuscriptCompanyDataFree.objects.get(id=manuscript_company_data_free.id)
        assert manuscript_company_data_free_test.name == "name update"

    def test_delete(self, create_manuscript_company_data_free):
        assert ManuscriptCompanyDataFree.objects.count() == 1
        create_manuscript_company_data_free.delete()
        assert ManuscriptCompanyDataFree.objects.count() == 0


# test manuscript_company_data_size
@pytest.mark.django_db
class TestManuscriptCompanyDataSite:
    def test_create(self, create_manuscript_company_data_size):
        assert ManuscriptCompanyDataSite.objects.count() == 1

    def test_update(self, create_manuscript_company_data_size):
        manuscript_company_data_size = create_manuscript_company_data_size
        manuscript_company_data_size.name = "name update"
        manuscript_company_data_size.save()

        manuscript_company_data_size_test = ManuscriptCompanyDataSite.objects.get(id=manuscript_company_data_size.id)
        assert manuscript_company_data_size_test.name == "name update"

    def test_delete(self, create_manuscript_company_data_size):
        assert ManuscriptCompanyDataSite.objects.count() == 1
        create_manuscript_company_data_size.delete()
        assert ManuscriptCompanyDataSite.objects.count() == 0


# test manuscript_student_relation
@pytest.mark.django_db
class TestManuscriptStudentRelation:
    def test_create(self, create_manuscript_student_relation):
        assert ManuscriptStudentRelation.objects.count() == 1

    def test_update(self, create_manuscript_student_relation):
        manuscript_student_relation = create_manuscript_student_relation
        manuscript_student_relation.remark = "remark update"
        manuscript_student_relation.save()

        manuscript_student_relation_test = ManuscriptStudentRelation.objects.get(id=manuscript_student_relation.id)
        assert manuscript_student_relation_test.remark == "remark update"

    def test_delete(self, create_manuscript_student_relation):
        assert ManuscriptStudentRelation.objects.count() == 1
        create_manuscript_student_relation.delete()
        assert ManuscriptStudentRelation.objects.count() == 0


# test manuscript_profile_feature_tag
@pytest.mark.django_db
class TestManuscriptProfileFeatureTag:
    def test_create(self, create_manuscript_profile_feature_tag):
        assert ManuscriptProfileFeatureTag.objects.count() == 1

    def test_update(self, create_manuscript_profile_feature_tag):
        manuscript_profile_feature_tag = create_manuscript_profile_feature_tag
        manuscript_profile_feature_tag.name = "name update"
        manuscript_profile_feature_tag.save()

        manuscript_profile_feature_tag_test = ManuscriptProfileFeatureTag.objects.get(
            id=manuscript_profile_feature_tag.id)
        assert manuscript_profile_feature_tag_test.name == "name update"

    def test_delete(self, create_manuscript_profile_feature_tag):
        assert ManuscriptProfileFeatureTag.objects.count() == 1
        create_manuscript_profile_feature_tag.delete()
        assert ManuscriptProfileFeatureTag.objects.count() == 0


# test manuscript_profile_job_type
@pytest.mark.django_db
class TestManuscriptProfileJobType:
    def test_create(self, create_manuscript_profile_job_type):
        assert ManuscriptProfileJobType.objects.count() == 1

    def test_update(self, create_manuscript_profile_job_type):
        manuscript_profile_job_type = create_manuscript_profile_job_type
        manuscript_profile_job_type.created_by = None
        manuscript_profile_job_type.save()

        manuscript_profile_job_type_test = ManuscriptProfileJobType.objects.get(id=manuscript_profile_job_type.id)
        assert manuscript_profile_job_type_test.created_by is None

    def test_delete(self, create_manuscript_profile_job_type):
        assert ManuscriptProfileJobType.objects.count() == 1
        create_manuscript_profile_job_type.delete()
        assert ManuscriptProfileJobType.objects.count() == 0


# test manuscript_profile_work_place
@pytest.mark.django_db
class TestManuscriptProfileWorkPlace:
    def test_create(self, create_manuscript_profile_work_place):
        assert ManuscriptProfileWorkPlace.objects.count() == 1

    def test_update(self, create_manuscript_profile_work_place):
        manuscript_profile_work_place = create_manuscript_profile_work_place
        manuscript_profile_work_place.created_by = None
        manuscript_profile_work_place.save()

        manuscript_profile_work_place_test = ManuscriptProfileWorkPlace.objects.get(id=manuscript_profile_work_place.id)
        assert manuscript_profile_work_place_test.created_by is None

    def test_delete(self, create_manuscript_profile_work_place):
        assert ManuscriptProfileWorkPlace.objects.count() == 1
        create_manuscript_profile_work_place.delete()
        assert ManuscriptProfileWorkPlace.objects.count() == 0


# test feed_category
@pytest.mark.django_db
class TestFeedCategory:
    def test_create(self, create_feed_category):
        assert FeedCategory.objects.count() == 1

    def test_update(self, create_feed_category):
        feed_category = create_feed_category
        feed_category.name = "name update"
        feed_category.save()

        feed_category_test = FeedCategory.objects.get(id=feed_category.id)
        assert feed_category_test.name == "name update"

    def test_delete(self, create_feed_category):
        assert FeedCategory.objects.count() == 1
        create_feed_category.delete()
        assert FeedCategory.objects.count() == 0


# test feed
@pytest.mark.django_db
class TestFeed:
    def test_create(self, create_feed):
        assert Feed.objects.count() == 1

    def test_update(self, create_feed):
        feed = create_feed
        feed.title = "title update"
        feed.save()

        feed_test = Feed.objects.get(id=feed.id)
        assert feed_test.title == "title update"

    def test_delete(self, create_feed):
        assert Feed.objects.count() == 1
        create_feed.delete()
        assert Feed.objects.count() == 0


# test manuscript_company_appeal
@pytest.mark.django_db
class TestManuscriptCompanyAppeal:
    def test_create(self, create_manuscript_company_appeal):
        assert ManuscriptCompanyAppeal.objects.count() == 1

    def test_update(self, create_manuscript_company_appeal):
        manuscript_company_appeal = create_manuscript_company_appeal
        manuscript_company_appeal.message = "message update"
        manuscript_company_appeal.save()

        manuscript_company_appeal_test = ManuscriptCompanyAppeal.objects.get(id=manuscript_company_appeal.id)
        assert manuscript_company_appeal_test.message == "message update"

    def test_delete(self, create_manuscript_company_appeal):
        assert ManuscriptCompanyAppeal.objects.count() == 1
        create_manuscript_company_appeal.delete()
        assert ManuscriptCompanyAppeal.objects.count() == 0


# test manuscript_company_appeal_point
@pytest.mark.django_db
class TestManuscriptCompanyAppealPoint:
    def test_create(self, create_manuscript_company_appeal_point):
        assert ManuscriptCompanyAppealPoint.objects.count() == 1

    def test_update(self, create_manuscript_company_appeal_point):
        manuscript_company_appeal_point = create_manuscript_company_appeal_point
        manuscript_company_appeal_point.message = "message update"
        manuscript_company_appeal_point.save()

        manuscript_company_appeal_point_test = ManuscriptCompanyAppealPoint.objects.get(
            id=manuscript_company_appeal_point.id)
        assert manuscript_company_appeal_point_test.message == "message update"

    def test_delete(self, create_manuscript_company_appeal_point):
        assert ManuscriptCompanyAppealPoint.objects.count() == 1
        create_manuscript_company_appeal_point.delete()
        assert ManuscriptCompanyAppealPoint.objects.count() == 0


# test feed_category_many
@pytest.mark.django_db
class TestFeedCategoryMany:
    def test_create(self, create_feed_category_many):
        assert FeedCategoryMany.objects.count() == 1

    def test_update(self, create_feed_category_many):
        feed_category_many = create_feed_category_many
        feed_category_many.feed = None
        feed_category_many.save()

        feed_category_many_test = FeedCategoryMany.objects.get(id=feed_category_many.id)
        assert feed_category_many_test.feed is None

    def test_delete(self, create_feed_category_many):
        assert FeedCategoryMany.objects.count() == 1
        create_feed_category_many.delete()
        assert FeedCategoryMany.objects.count() == 0


# test pickup_company
@pytest.mark.django_db
class TestPickupCompany:
    def test_create(self, create_pickup_company):
        assert PickupCompany.objects.count() == 1

    def test_update(self, create_pickup_company):
        pickup_company = create_pickup_company
        pickup_company.year = 2022
        pickup_company.save()

        pickup_company_test = PickupCompany.objects.get(id=pickup_company.id)
        assert pickup_company_test.year == 2022

    def test_delete(self, create_pickup_company):
        assert PickupCompany.objects.count() == 1
        create_pickup_company.delete()
        assert PickupCompany.objects.count() == 0


# test company_feed_notify
@pytest.mark.django_db
class TestCompanyFeedNotify:
    def test_create(self, create_company_feed_notify):
        assert CompanyFeedNotify.objects.count() == 1

    def test_update(self, create_company_feed_notify):
        company_feed_notify = create_company_feed_notify
        company_feed_notify.company = None
        company_feed_notify.save()

        company_feed_notify_test = CompanyFeedNotify.objects.get(id=company_feed_notify.id)
        assert company_feed_notify_test.company is None

    def test_delete(self, create_company_feed_notify):
        assert CompanyFeedNotify.objects.count() == 1
        create_company_feed_notify.delete()
        assert CompanyFeedNotify.objects.count() == 0
