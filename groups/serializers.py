from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'description', 'project', 'no_progress',  'in_progress', 'completed', 'created_at', 'slug')
