from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# from .app.share_resource.users.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)


app_name = "users"
urlpatterns = router.urls
