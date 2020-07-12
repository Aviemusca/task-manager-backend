from django.contrib import admin

from .models import Task
from .forms import TaskForm


class TaskAdmin(admin.ModelAdmin):
    model = Task
    form = TaskForm
    list_display = (
        "title",
        "group",
        "get_project",
        "description",
        "no_progress",
        "in_progress",
        "completed",
        "created_at",
        "slug",
    )

    def get_project(self, obj):
        return obj.group.project

    # Rename Admin Column
    get_project.short_description = "project"


admin.site.register(Task, TaskAdmin)
