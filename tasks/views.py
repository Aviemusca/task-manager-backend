from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TaskSerializer

from .models import Task
from groups.models import Group


class TaskViewSet(viewsets.ModelViewSet):
    """ A rest api viewset for CRUD task operations in a given project task group """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_target_group(self, **kwargs):
        """ Returns the target group for the viewset from the url kwargs """
        group_pk = kwargs.get("group_pk", None)
        target_group = get_object_or_404(Group, pk=group_pk)
        return target_group

    def get_target_task(self, queryset, **kwargs):
        """ Returns the target task from a group-level queryset and the
        task pk in the url kwargs """
        task_pk = kwargs.get("pk", None)
        target_task = get_object_or_404(queryset, pk=task_pk)
        return target_task

    def list(self, request, **kwargs):
        """ list (get) all tasks of a given group """
        target_group = self.get_target_group(**kwargs)
        queryset = Task.objects.filter(group=target_group)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        """ Retrieve (get) a specific task in a given group """
        target_group = self.get_target_group(**kwargs)
        queryset = Task.objects.filter(group=target_group)
        target_task = self.get_target_task(queryset, **kwargs)
        serializer = self.get_serializer(target_task)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        """ Create (post) a task in a given group """
        data = request.data.copy()

        # Get the target group from url kwargs
        target_group = self.get_target_group(**kwargs)

        # Make request data mutable to save group in serializer
        data["group"] = target_group.id

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
        """ Update (patch) a specific task in a given project """
        target_group = self.get_target_group(**kwargs)
        queryset = Task.objects.filter(group=target_group)
        target_task = self.get_target_task(queryset, **kwargs)
        serializer = self.get_serializer(target_task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, **kwargs):
        """ Delete (delete) a task in a given group """
        target_group = self.get_target_group(**kwargs)
        queryset = Task.objects.filter(group=target_group)
        target_task = self.get_target_task(queryset, **kwargs)
        self.perform_destroy(target_task)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
