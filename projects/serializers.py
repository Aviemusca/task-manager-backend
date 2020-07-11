from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "owner",
            "description",
            "no_progress",
            "in_progress",
            "completed",
            "created_at",
            "slug",
        )
