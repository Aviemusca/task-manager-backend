from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet


router = routers.DefaultRouter()
router.register("viewset", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<slug:project_slug>/groups/", include("groups.urls")),
    path("<slug:project_slug>/tasks/", include("tasks.urls"))
]
