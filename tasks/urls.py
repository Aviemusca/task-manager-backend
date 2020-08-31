from django.urls import path, include

from rest_framework import routers

from .views import GroupTaskViewSet, ProjectTaskViewSet

router = routers.DefaultRouter()
router.register("viewset", GroupTaskViewSet)
router.register("project-task-viewset", ProjectTaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
