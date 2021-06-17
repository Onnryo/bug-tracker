from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner")
    members = models.ManyToManyField(User, related_name="members")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
