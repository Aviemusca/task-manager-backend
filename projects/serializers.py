from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    dateCreated = serializers.DateTimeField(
            source="created_at", format="%Y-%m-%d %H:%M:%S", read_only=True
    )
    description = serializers.CharField(required=False, allow_blank=True)
    state = serializers.IntegerField(required=False)
    deadline = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "owner",
            "description",
            "state",
            "dateCreated",
            "deadline",
            "slug",
        )
