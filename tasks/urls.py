from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TaskListCreateView, TaskDetailUpdateDeleteView, TaskStatsView,
                    SubTaskListCreateView, SubTaskDetailUpdateDeleteView, CategoryViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('', include(router.urls)),
]
