import logging

# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# from django.core.cache import cache

# from app.share_resources.users.models import Admin, Company, Student

logger = logging.getLogger()
User = get_user_model()


class AuthBackend(ModelBackend):
    """Authen backend for Student, Company, Employee"""

    def authenticate(self, request, username, password, usertype, **kwargs):
        # get user by username
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logger.info(f"{username} is not exist")
            return None

        # default validate
        if not user.check_password(password):
            logger.info(f"{username} password is incorrect")
            return None
        if not self.user_can_authenticate(user):
            logger.info(f"{username} is not active")
            return None

        # custom validate
        if user.type != usertype:
            return None
        if usertype == User.TYPES.STUDENT:
            if user.is_closed == 1:
                logger.warning(f"{username} is closed")
                return None
            if user.is_locked == 1:
                logger.warning(f"{username} is locked")
                return None
            if user.is_deleted == 1:
                logger.warning(f"{username} is deleted")
                return None
        # elif usertype == User.TYPES.COMPANY:
        #     pass
        # elif usertype == User.TYPES.ADMIN:
        #     pass
        return user

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
