from django.urls import path
from .views import task_stats, \
SubTaskListCreateView, SubTaskRetrieveUpdateDeleteView,\
TaskListCreateView, TaskRetrieveUpdateDeleteView

app_name = 'tasks'

urlpatterns = [
    path('task/', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('stats/', task_stats, name="task-stats"),
    path('subtasks/', SubTaskListCreateView.as_view(), name="subtask-list-create"),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDeleteView.as_view(), name="subtask-detail-update-delete")
]