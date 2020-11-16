from functools import wraps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from django.contrib.auth.views import redirect_to_login

User = get_user_model()


def login_required_factory(usertype):

    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.type == usertype:
                return view_func(request, *args, **kwargs)

            # if login fail redirect to login_url
            # redirect_url form `{STUDENT_LOGIN_URL}?{REDIRECT_FIELD_NAME}={request.path}`
            path = request.path
            resolved_login_url = resolve_url(settings.LOGIN_URL)
            redirect_field_name = settings.REDIRECT_FIELD_NAME
            return redirect_to_login(path, resolved_login_url, redirect_field_name)

        return wrapped_view

    return decorator


student_login_required = login_required_factory(User.TYPES.STUDENT)
company_login_required = login_required_factory(User.TYPES.COMPANY)
admin_login_required = login_required_factory(User.TYPES.ADMIN)

# example:
# @student_login_required
# def student_profile(request):
#     pass
