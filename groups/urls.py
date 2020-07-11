from django.urls import path, include

from rest_framework import routers

from .views import GroupViewSet

router = routers.DefaultRouter()
router.register("viewset", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
