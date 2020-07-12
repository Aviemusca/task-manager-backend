from django.db import models

from groups.models import Group

from utils.slugs import unique_slugify


class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="tasks")
    no_progress = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title[:110]
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)
