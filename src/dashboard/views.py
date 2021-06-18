from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'dashboard/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-modified']
    paginate_by = 5


def about(request):
    ctx = {
        'title': 'About'
    }
    return render(request, 'dashboard/about.html', ctx)
