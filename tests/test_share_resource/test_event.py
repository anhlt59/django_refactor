import pytest

from app.share_resources.event.models import Event


@pytest.mark.django_db
class TestEvent:
    def test_create(self, create_event):
        assert Event.objects.count() == 1

    def test_update(self, create_event):
        event = Event.objects.get(target_year=2022)
        event.class_division = "class division 2"
        event.save()

        event_test = Event.objects.get(target_year=2022)

        assert event_test.class_division == "class division 2"

    def test_delete(self, create_event):
        assert Event.objects.count() == 1
        Event.objects.get(target_year=2022).delete()
        assert Event.objects.count() == 0
