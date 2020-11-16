from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path


# # if you used viewset
# if settings.DEBUG:
#     router = DefaultRouter()
# else:
#     router = SimpleRouter()
#
# router.register("users", UserViewSet)

urlpatterns = [
    # path("", include("")),
] # + router.urls
