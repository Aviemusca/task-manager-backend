from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "group",
            "no_progress",
            "in_progress",
            "completed",
            "created_at",
            "slug",
        )
