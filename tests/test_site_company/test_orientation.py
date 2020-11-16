import pytest

# test orientation
from app.site_company.orientation.models import Orientation, OrientationPlan, ReservedOrientation


@pytest.mark.django_db
class TestOrientation:
    def test_create(self, create_orientation):
        assert Orientation.objects.count() == 1

    def test_update(self, create_orientation):
        orientation = create_orientation
        orientation.name = "name update"
        orientation.save()

        orientation_test = Orientation.objects.get(id=orientation.id)
        assert orientation_test.name == "name update"

    def test_delete(self, create_orientation):
        assert Orientation.objects.count() == 1
        create_orientation.delete()
        assert Orientation.objects.count() == 0


# test orientation_plan
@pytest.mark.django_db
class TestOrientationPlan:
    def test_create(self, create_orientation_plan):
        assert OrientationPlan.objects.count() == 1

    def test_update(self, create_orientation_plan):
        orientation_plan = create_orientation_plan
        orientation_plan.place = "place update"
        orientation_plan.save()

        orientation_plan_test = OrientationPlan.objects.get(id=orientation_plan.id)
        assert orientation_plan_test.place == "place update"

    def test_delete(self, create_orientation_plan):
        assert OrientationPlan.objects.count() == 1
        create_orientation_plan.delete()
        assert OrientationPlan.objects.count() == 0


# test reserved_orientation
@pytest.mark.django_db
class TestReservedOrientation:
    def test_create(self, create_reserved_orientation):
        assert ReservedOrientation.objects.count() == 1

    def test_update(self, create_reserved_orientation):
        reserved_orientation = create_reserved_orientation
        reserved_orientation.number_of_day = 2
        reserved_orientation.save()

        reserved_orientation_test = ReservedOrientation.objects.get(id=reserved_orientation.id)
        assert reserved_orientation_test.number_of_day == 2

    def test_delete(self, create_reserved_orientation):
        assert ReservedOrientation.objects.count() == 1
        create_reserved_orientation.delete()
        assert ReservedOrientation.objects.count() == 0
