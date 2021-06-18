from django.urls import path
from .views import (
    ProjectListView,
    about
)

urlpatterns = [
    path('', ProjectListView.as_view(), name="dashboard-home"),
    path('about/', about, name="dashboard-about"),
]
