from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import GroupSerializer

from .models import Group
from projects.models import Project


class GroupViewSet(viewsets.ModelViewSet):
    """ A rest api viewset for CRUD group operations in a given project """

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_url_kwarg = "group_pk"

    def get_target_project(self, project_slug):
        """ Returns the target project of the viewset from the url kwargs """
        project = get_object_or_404(Project, slug=project_slug)
        return project

    def get_target_group_qs(self, project_slug):
        """ Returns the group queryset of the target project """
        project = self.get_target_project(project_slug)
        queryset = Group.objects.filter(project=project)
        return queryset

    def get_target_group(self, project_slug, group_pk):
        """ Returns the target group from a project-level queryset
        and the group pk in the url kwargs """
        queryset = self.get_target_group_qs(project_slug)
        group = get_object_or_404(queryset, pk=group_pk)
        return group

    def list(self, request, project_slug=None):
        """ list (get) all groups of a given project"""
        queryset = self.get_target_group_qs(project_slug)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, project_slug=None, group_pk=None):
        """ Retrieve (get) a specific group in a given project """
        group = self.get_target_group(project_slug, group_pk)
        serializer = self.get_serializer(group)
        return Response(serializer.data)

    def create(self, request, project_slug=None):
        """ Create (post) a group in a given project """
        data = request.data.copy()

        # Add the target project to the request data
        project = self.get_target_project(project_slug)
        data["project"] = project.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, project_slug=None, group_pk=None):
        """ Partially update (patch) a group in a project """
        group = self.get_target_group(project_slug, group_pk)
        serializer = self.get_serializer(group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, project_slug=None, group_pk=None):
        """ Delete (delete) a group in a given project """
        group = self.get_target_group(project_slug, group_pk)
        self.perform_destroy(group)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
