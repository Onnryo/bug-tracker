from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner")
    members = models.ManyToManyField(User, related_name="members")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})
