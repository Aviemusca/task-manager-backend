from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from utils.slugs import unique_slugify

class ProjectManager(models.Manager):
    """ Custom project model manager """
    def get_queryset(self):
        return super().get_queryset().order_by("created_at")


class Project(models.Model):
    """ A class to manage overall projects, which are collections of groups of tasks """
    STATES = ((0, "no progress"),
            (1, "in progress"), (2, "completed"))

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="projects"
    )
    description = models.TextField(default="")
    state = models.IntegerField(choices=STATES, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    completion = models.FloatField(default=0)
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    objects = ProjectManager()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)

    def get_num_tasks(self):
        """ Returns the total number of tasks in the project """
        return sum([group.tasks.count() for group in self.groups.all()])

    def get_completion(self):
        """ Returns the task completion rate """
        completed_tasks = sum([1 for group in self.groups.all() for task in group.tasks.all() if task.state == 2])
        return round(completed_tasks/self.get_num_tasks(), 4)

    def update_completion(self):
        self.completion = self.get_completion()
        self.save()
