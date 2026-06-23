from django.urls import path
from .views import task_stats, \
SubTaskListCreateView, SubTaskRetrieveUpdateDeleteView,\
TaskListCreateView, TaskRetrieveUpdateDeleteView, CategoryViewSet

from rest_framework.routers import DefaultRouter

app_name = 'tasks'

router = DefaultRouter()

router.register('category', CategoryViewSet)

urlpatterns = [
    path('task/', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail-update-delete'),

    path('stats/', task_stats, name="task-stats"),

    path('subtasks/', SubTaskListCreateView.as_view(), name="subtask-list-create"),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDeleteView.as_view(), name="subtask-detail-update-delete")
]

urlpatterns += router.urls