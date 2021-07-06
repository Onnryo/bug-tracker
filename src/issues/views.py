from django.conf.urls import url
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from projects.models import Project
from .models import Issue


class IssueDetailView(UserPassesTestMixin, DetailView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    context_object_name = 'issue'
    # template_name = 'projects/project_detail.html'

    def test_func(self):
        issue = self.get_object()
        return issue.parent_project.is_public or self.request.user in issue.parent_project.members.all()


class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    fields = ['title', 'description']
    # template_name = 'projects/project_form.html'
    # success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        print(self.project)
        form.instance.parent_project = self.project
        form.instance.author = self.request.user

        response = super().form_valid(form)
        return response

    def test_func(self):
        self.project = Project.objects.filter(pk=self.kwargs['pk'])[:1].get()
        return self.project.is_public or self.request.user in self.project.members.all()


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    fields = ['title', 'description']
    # template_name = 'projects/project_form.html'

    def form_valid(self, form):
        form.instance.project = self.kwargs['pk']
        form.instance.author = self.request.user

        response = super().form_valid(form)
        return response

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author or self.request.user in issue.parent_project.members.all()


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    # template_name = 'projects/project_confirm_delete.html'

    def get_success_url(self):
        issue = self.get_object()
        return reverse_lazy('project-detail', kwargs={'pk': issue.parent_project.id})

    def test_func(self):
        issue = self.get_object()
        return self.request.user in issue.parent_project.members.all()
