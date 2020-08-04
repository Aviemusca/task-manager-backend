from django.db import models

from utils.slugs import unique_slugify

from projects.models import Project


class GroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("created_at")


class Group(models.Model):
    """ A class to manage a group of tasks within a given project """

    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="groups"
    )
    no_progress = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    objects = GroupManager()

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)
