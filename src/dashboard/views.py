from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'dashboard/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-modified']
    paginate_by = 5

    def get_queryset(self):
        print(self.request.user.pk)
        is_public = Q(is_public=True)
        is_member = Q(members__pk=self.request.user.pk)
        return Project.objects.filter(is_public | is_member).order_by('-modified')
        # return Project.objects.filter(owner=user).order_by('-modified')


def about(request):
    ctx = {
        'title': 'About'
    }
    return render(request, 'dashboard/about.html', ctx)
