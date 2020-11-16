import pytest

from app.site_admin.admin_profile.models import *

# test special_feature


@pytest.fixture
def create_special_feature():
    special_feature = SpecialFeature.objects.create(
        year=2049,
        for_event_flg=22,
        image="egaeg",
        title="title",
        outline="outline",
        number_listed_company=12,
        pv_count=12,
        created="2999-10-10",
        description="teat",
    )
    return special_feature


@pytest.mark.django_db
class TestSpecialFeature:
    def test_create(self, create_special_feature):
        assert SpecialFeature.objects.count() == 1

    def test_update(self, create_special_feature):
        special_feature = create_special_feature
        special_feature.title = "title update"
        special_feature.save()

        special_feature_test = SpecialFeature.objects.get(id=special_feature.id)
        assert special_feature_test.title == "title update"

    def test_delete(self, create_special_feature):
        assert SpecialFeature.objects.count() == 1
        create_special_feature.delete()
        assert SpecialFeature.objects.count() == 0


@pytest.fixture
def create_special_feature_appeal_point(create_manuscript, create_special_feature):
    special_feature_appeal_point = SpecialFeatureAppealPoint.objects.create(
        point_1="point",
        point_2="oint",
        point_3="wae",
        type=12,
        year=2000,
        special_feature=create_special_feature,
        manuscript=create_manuscript,
    )
    return special_feature_appeal_point


@pytest.mark.django_db
class TestSpecialFeatureAppealPoint:
    def test_create(self, create_special_feature_appeal_point):
        assert SpecialFeatureAppealPoint.objects.count() == 1

    def test_update(self, create_special_feature_appeal_point):
        special_feature_appeal_point = create_special_feature_appeal_point
        special_feature_appeal_point.year = 3255
        special_feature_appeal_point.save()

        special_feature_appeal_point_test = SpecialFeatureAppealPoint.objects.get(
            id=special_feature_appeal_point.id
        )
        assert special_feature_appeal_point_test.year == 3255

    def test_delete(self, create_special_feature_appeal_point):
        assert SpecialFeatureAppealPoint.objects.count() == 1
        create_special_feature_appeal_point.delete()
        assert SpecialFeatureAppealPoint.objects.count() == 0
