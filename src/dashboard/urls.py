from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="dashboard-home"),
    path('about/', views.about, name="dashboard-about"),
]
