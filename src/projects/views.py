from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from users.models import CustomUser


class UserProjectListView(ListView):
    model = Project
    template_name = 'projects/user_projects.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(
            CustomUser, username=self.kwargs.get('username'))
        is_public = Q(is_public=True)
        is_member = Q(members__pk=self.request.user.pk)
        return Project.objects.filter(owner=user).filter(is_public | is_member).order_by('-modified')


class ProjectDetailView(UserPassesTestMixin, DetailView):
    model = Project
    # template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def test_func(self):
        project = self.get_object()
        return project.is_public or self.request.user in project.members.all()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    # template_name = 'projects/project_form.html'
    fields = ['name', 'members', 'is_public']
    # success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    # template_name = 'projects/project_form.html'
    fields = ['name', 'members', 'is_public']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.owner


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    # template_name = 'projects/project_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.owner
