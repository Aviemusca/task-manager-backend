from django.contrib import admin

from .models import Project
from .forms import ProjectForm


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    form = ProjectForm
    list_display = (
        "title",
        "owner",
        "description",
        "no_progress",
        "in_progress",
        "completed",
        "completion",
        "created_at",
        "slug",
    )


admin.site.register(Project, ProjectAdmin)
