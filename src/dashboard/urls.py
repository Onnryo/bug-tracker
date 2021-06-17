from django.urls import path
from .views import ProjectListView
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name="dashboard-home"),
    path('about/', views.about, name="dashboard-about"),
]
