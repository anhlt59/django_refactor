import pytest

from app.site_company.company_profile.models import CompanyProfile, SpecialFeature


# test company_profile
@pytest.mark.django_db
class TestCompanyProfile:
    def test_create(self, create_company_profile):
        assert CompanyProfile.objects.count() == 1

    def test_update(self, create_company_profile):
        company = create_company_profile
        company.name = "name update"
        company.save()

        company_test = CompanyProfile.objects.get(id=company.id)
        assert company_test.name == "name update"

    def test_delete(self, create_company_profile):
        assert CompanyProfile.objects.count() == 1
        create_company_profile.delete()
        assert CompanyProfile.objects.count() == 0


# test special_feature
@pytest.mark.django_db
class TestSpecialFeature:
    def test_create(self, create_special_feature):
        assert SpecialFeature.objects.count() == 1

    def test_update(self, create_special_feature):
        special_feature = create_special_feature
        special_feature.year = 2022
        special_feature.save()

        special_feature_test = SpecialFeature.objects.get(id=special_feature.id)
        assert special_feature_test.year == 2022

    def test_delete(self, create_special_feature):
        assert SpecialFeature.objects.count() == 1
        create_special_feature.delete()
        assert SpecialFeature.objects.count() == 0
