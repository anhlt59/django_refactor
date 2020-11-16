import pytest

from app.share_resources.users.models import Student, Company, Admin


# test student
@pytest.mark.django_db
class TestStudent:
    def test_create(self, create_student):
        assert Student.objects.count() == 1

    def test_update(self, create_student):
        student = create_student
        student.email = "test_update@gmail.com"
        student.save()

        student_test = Student.objects.get(id=create_student.id)
        assert student_test.email == "test_update@gmail.com"

    def test_delete(self, create_student):
        assert Student.objects.count() == 1
        create_student.delete()
        assert Student.objects.count() == 0


# test company
@pytest.mark.django_db
class TestCompany:
    def test_create(self, create_company):
        assert Company.objects.count() == 1

    def test_update(self, create_company):
        company = create_company
        company.email = "test_update@gmail.com"
        company.save()

        company_test = Company.objects.get(id=create_company.id)
        assert company_test.email == "test_update@gmail.com"

    def test_delete(self, create_company):
        assert Company.objects.count() == 1
        create_company.delete()
        assert Company.objects.count() == 0


# test admin
@pytest.mark.django_db
class TestAdmin:
    def test_create(self, create_admin):
        assert Admin.objects.count() == 1

    def test_update(self, create_admin):
        admin = create_admin
        admin.email = "test_update@gmail.com"
        admin.save()

        admin_test = Admin.objects.get(id=create_admin.id)
        assert admin_test.email == "test_update@gmail.com"

    def test_delete(self, create_admin):
        assert Admin.objects.count() == 1
        create_admin.delete()
        assert Admin.objects.count() == 0
