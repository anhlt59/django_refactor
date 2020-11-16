import pytest

from app.site_admin.admin_profile.models import Employee


@pytest.mark.django_db
class TestEmployee:
    def test_create(self, create_employee):
        assert Employee.objects.count() == 1

    def test_update(self, create_employee):
        employee = create_employee
        employee.user = "user update"
        employee.save()
        employee_test = Employee.objects.get(id=employee.id)
        assert employee_test.user == "user update"

    def test_delete(self, create_employee):
        assert Employee.objects.count() == 1
        create_employee.delete()
        assert Employee.objects.count() == 0
