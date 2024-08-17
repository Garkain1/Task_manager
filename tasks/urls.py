from django.urls import path
from .views import TaskCreateView, TaskListView, TaskStatsView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
]
