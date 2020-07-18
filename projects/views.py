from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer

from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """ A rest api viewset for CRUD project operations owned by a given user """

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "slug"
    lookup_url_kwarg = "project_slug"

    def get_target_project(self, request, project_slug=None):
        """ Returns the target project for the viewset from
        the user project qs and the url_kwarg """
        queryset = request.user.projects.all()
        project = get_object_or_404(queryset, slug=project_slug)
        return project

    def list(self, request):
        queryset = request.user.projects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, project_slug=None):
        project = self.get_target_project(request, project_slug)
        serializer = self.get_serializer(project)
        return Response(serializer.data)

    def create(self, request):
        """ Create (post) a project for a given user """
        data = request.data.copy()
        data["owner"] = request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, project_slug=None):
        project = self.get_target_project(request, project_slug)
        serializer = self.get_serializer(project, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data)

    def destroy(self, request, project_slug=None):
        project = self.get_target_project(request, project_slug)
        self.perform_destroy(project)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
