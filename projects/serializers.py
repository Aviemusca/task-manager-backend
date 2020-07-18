from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    dateCreated = serializers.DateTimeField(source='created_at', format="%B %d, %Y", required=False)
    noProgress = serializers.BooleanField(source='no_progress', required=False)
    inProgress = serializers.BooleanField(source='in_progress', required=False)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "owner",
            "description",
            "noProgress",
            "inProgress",
            "completed",
            "dateCreated",
            "slug",
        )
