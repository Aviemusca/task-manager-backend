from django.contrib import admin

from .models import Group
from .forms import GroupForm


class GroupAdmin(admin.ModelAdmin):
    model = Group
    form = GroupForm
    list_display = (
        "title",
        "project",
        "description",
        "no_progress",
        "in_progress",
        "completed",
        "created_at",
        "slug",
    )


admin.site.register(Group, GroupAdmin)
