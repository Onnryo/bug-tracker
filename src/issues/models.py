from django.db import models
from django.urls import reverse
from projects.models import Project
from users.models import CustomUser


class Issue(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, related_name="author", null=True)
    parent_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project")
    key = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def Meta(self):
        unique_together = ("key", "parent_project")

    def save(self, *args, **kwargs):
        key = self.cal_key(self.parent_project)
        self.key = key
        super(Issue, self).save(*args, **kwargs)

    def cal_key(self, fk):
        present_keys = Issue.objects.filter(parent_project=fk).order_by(
            '-key').values_list('key', flat=True)
        if present_keys:
            return present_keys[0]+1
        else:
            return 0

    def get_absolute_url(self):
        return reverse("issue-detail", kwargs={"pk": self.parent_project.pk, "issue_pk": self.pk})
