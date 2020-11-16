from django import template
from django.db.models import Q

# from companies.models import Company
# from employee.models import Employee

register = template.Library()


@register.filter
def get_role(value):
    try:
        employee = Employee.objects.get(user_id=value)
        if not employee.role_id:
            return 0
        return employee.role_id.id
    except Employee.DoesNotExist:
        return 0


@register.filter
def get_company(value):
    try:
        employee = Employee.objects.get(user_id=value)
        sale1 = Q(staff_name1_id=employee.id)
        sale2 = Q(staff_name2_id=employee.id)
        companies = [company.id for company in Company.objects.filter(sale1 | sale2)]
    except (Employee.DoesNotExist, Company.DoesNotExist):
        companies = []
    return companies
