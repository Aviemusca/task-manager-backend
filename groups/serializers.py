from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    projectSlug = serializers.CharField(source="project.slug", read_only=True)
    dateCreated = serializers.DateTimeField(
        source="created_at", format="%B %d, %Y", read_only=True
    )
    noProgress = serializers.BooleanField(source="no_progress", required=False)
    inProgress = serializers.BooleanField(source="in_progress", required=False)
    completion = serializers.FloatField(required=False)

    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "description",
            "project",
            "projectSlug",
            "noProgress",
            "inProgress",
            "completed",
            "completion",
            "dateCreated",
            "slug",
        )
