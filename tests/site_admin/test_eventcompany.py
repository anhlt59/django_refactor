import pytest

from app.site_admin.admin_profile.models import *

# test event_company


@pytest.mark.django_db
class TestConfigPush:
    def test_create(self, create_event_company):
        assert EventCompany.objects.count() == 1

    def test_update(self, create_event_company):
        event_company = create_event_company
        event_company.phonetic = "phonetic update"
        event_company.save()

        event_company_test = EventCompany.objects.get(id=event_company.id)
        assert event_company_test.phonetic == "phonetic update"

    def test_delete(self, create_event_company):
        assert EventCompany.objects.count() == 1
        create_event_company.delete()
        assert EventCompany.objects.count() == 0


@pytest.mark.django_db
class TestEventDataFree:
    def test_create(self, create_event_data_free):
        assert EventDataFree.objects.count() == 1

    def test_update(self, create_event_data_free):
        event_data_free = create_event_data_free
        event_data_free.name = "name update"
        event_data_free.save()

        event_data_free_test = EventDataFree.objects.get(id=event_data_free.id)
        assert event_data_free_test.name == "name update"

    def test_delete(self, create_event_data_free):
        assert EventDataFree.objects.count() == 1
        create_event_data_free.delete()
        assert EventDataFree.objects.count() == 0


@pytest.mark.django_db
class TestEventCompanyField:
    def test_create(self, create_event_company_field):
        assert EventCompanyField.objects.count() == 1

    def test_update(self, create_event_company_field):
        event_company_field = create_event_company_field
        event_company_field.field_value = 1
        event_company_field.save()

        event_company_field_test = EventCompanyField.objects.get(
            id=event_company_field.id
        )
        assert event_company_field_test.field_value == 1

    def test_delete(self, create_event_company_field):
        assert EventCompanyField.objects.count() == 1
        create_event_company_field.delete()
        assert EventCompanyField.objects.count() == 0


@pytest.mark.django_db
class EventCompanyStudent:
    def test_create(self, create_event_company_field):
        assert EventCompanyField.objects.count() == 1

    def test_update(self, create_event_company_field):
        event_company_field = create_event_company_field
        event_company_field.date_join = "2011-5-5"
        event_company_field.save()

        event_company_field_test = EventCompanyField.objects.get(
            id=event_company_field.id
        )
        assert event_company_field_test.field_name == "2020-5-5"

    def test_delete(self, create_event_company_field):
        assert EventCompanyField.objects.count() == 1
        create_event_company_field.delete()
        assert EventCompanyField.objects.count() == 0
