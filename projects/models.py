from django.db import models

from django.contrib.auth import get_user_model

from utils.slugs import unique_slugify


class Project(models.Model):
    """ A class to manage overall projects, which are collections of groups of tasks """

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="projects"
    )
    description = models.TextField(default="")
    no_progress = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)