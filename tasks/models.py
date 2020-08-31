from django.db import models
from datetime import datetime, timedelta

from groups.models import Group

from utils.slugs import unique_slugify


class TaskManager(models.Manager):
    """ Custom task model manager """

    def get_queryset(self):
        return super().get_queryset().order_by("created_at")

    def project(self, **kwargs):
        """ Returns all tasks of a given project """
        if kwargs.get("pk"):
            return super().get_queryset().filter(group__project__pk=kwargs.get("pk"))
        elif kwargs.get("slug"):
            return super().get_queryset().filter(group__project__slug=kwargs.get("slug"))
        else:
            raise Exception(f"Lookup kwarg not recognized. The provided kwargs were {kwargs}.")


class Task(models.Model):
    # Task state choices
    STATES = ((0, "no progress"), (1, "in progress"), (2, "completed"))
    title = models.CharField(max_length=300)
    description = models.TextField(default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="tasks")
    state = models.IntegerField(choices=STATES, default=0)
    archived = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(default=5)
    difficulty = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    objects = TaskManager()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title[:110]
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)
        self.update_completions()

    def update_completions(self):
        project = self.group.project
        project.update_completion()
        self.group.update_completion()

