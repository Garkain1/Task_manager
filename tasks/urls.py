from django.urls import path
from .views import (TaskListCreateView, TaskDetailUpdateDeleteView, TaskStatsView,
                    SubTaskListCreateAPIView, SubTaskDetailUpdateDeleteAPIView)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtasks/', SubTaskListCreateAPIView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteAPIView.as_view(), name='subtask-detail-update-delete'),
]
