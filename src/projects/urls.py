from django.urls import path, include
from .views import (
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    UserProjectListView
)

urlpatterns = [
    path('<int:pk>/issue/', include('issues.urls')),
    path('<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('new/', ProjectCreateView.as_view(), name="project-create"),
    path('user/<str:username>/', UserProjectListView.as_view(), name="user-projects"),
]
