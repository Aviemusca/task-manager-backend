from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    projectSlug = serializers.CharField(source="group.project.slug", read_only=True)
    groupId = serializers.IntegerField(source="group.id", read_only=True)
    groupTitle = serializers.CharField(source="group.title", read_only=True)
    dateCreated = serializers.DateTimeField(
            source="created_at", format="%Y-%m-%d %H:%M:%S", read_only=True
    )
    description = serializers.CharField(required=False, allow_blank=True)
    state = serializers.IntegerField(required=False)
    archived = serializers.BooleanField(required=False)
    priority = serializers.IntegerField(required=False)
    difficulty = serializers.IntegerField(required=False)
    deadline = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "group",
            "groupTitle",
            "projectSlug",
            "groupId",
            "dateCreated",
            "state",
            "archived",
            "priority",
            "difficulty",
            "deadline",
        )

