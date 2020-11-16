from django.conf import settings
from django.middleware.locale import LocaleMiddleware
from django.urls import reverse
from django.utils import translation


class CustomLocaleMiddleware(LocaleMiddleware):
    """Enable locale only on student-site"""

    def process_request(self, request):
        # /2022
        student_site_url = reverse("student-site")

        if request.path.startswith(student_site_url):
            super().process_request(request)
        else:
            # default ja
            language = settings.LANGUAGE_CODE
            translation.activate(language)
            request.LANGUAGE_CODE = translation.get_language()
