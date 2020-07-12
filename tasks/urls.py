from django.urls import path, include

from rest_framework import routers

from .views import TaskViewSet

router = routers.DefaultRouter()
router.register("viewset", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
