from django.db import models

from groups.models import Group

from utils.slugs import unique_slugify


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("created_at")


class Task(models.Model):
    # Task state choices
    STATES = ((0, "no progress"), (1, "in progress"), (2, "completed"))

    title = models.CharField(max_length=300)
    description = models.TextField(default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="tasks")
    state = models.IntegerField(choices=STATES, default=0)
    priority = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
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
