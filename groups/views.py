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

    def get_target_project(self, **kwargs):
        """ Returns the target project for the viewset from the url kwargs """
        project_pk = kwargs.get("project_pk", None)
        target_project = get_object_or_404(Project, pk=project_pk)
        return target_project

    def get_target_group(self, queryset, **kwargs):
        """ Returns the target group from a project-level queryset and the group pk in the url kwargs """
        group_pk = kwargs.get("pk", None)
        target_group = get_object_or_404(queryset, pk=group_pk)
        return target_group

    def list(self, request, **kwargs):
        """ list (get) all groups of a given project"""
        target_project = self.get_target_project(**kwargs)
        queryset = Group.objects.filter(project=target_project)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        """ Retrieve (get) a specific group in a given project """
        target_project = self.get_target_project(**kwargs)
        queryset = Group.objects.filter(project=target_project)
        target_group = self.get_target_group(queryset, **kwargs)
        serializer = self.get_serializer(target_group)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        """ Create (post) a group in a given project """
        data = request.data

        # Get the target project from url kwargs
        target_project = self.get_target_project(**kwargs)

        # Make request data mutable to save project in serializer
        data._mutable = True
        data["project"] = target_project.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, **kwargs):
        """ Update (patch) a specific group in a given project """
        target_project = self.get_target_project(**kwargs)
        queryset = Group.objects.filter(project=target_project)
        target_group = self.get_target_group(queryset, **kwargs)
        serializer = self.get_serializer(target_group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, **kwargs):
        """ Delete (delete) a group in a given project """
        target_project = self.get_target_project(**kwargs)
        queryset = Group.objects.filter(project=target_project)
        target_group = self.get_target_group(queryset, **kwargs)
        self.perform_destroy(target_group)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
