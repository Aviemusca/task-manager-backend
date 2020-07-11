from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer

from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request):
        queryset = request.user.projects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = request.user.projects.all()
        target_project = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(target_project)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def partial_update(self, request, pk=None):
        queryset = request.user.projects.all()
        target_project = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(
            target_project, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = request.user.projects.all()
        target_project = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(target_project)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
