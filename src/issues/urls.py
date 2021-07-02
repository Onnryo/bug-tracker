from django.urls import path
from .views import (
    IssueDetailView,
    IssueUpdateView,
    IssueDeleteView,
    IssueCreateView,
)

urlpatterns = [
    path('<int:issue_pk>/', IssueDetailView.as_view(), name="issue-detail"),
    path('<int:issue_pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
    path('<int:issue_pk>/delete/', IssueDeleteView.as_view(), name='issue-delete'),
    path('new/', IssueCreateView.as_view(), name="issue-create"),
]
