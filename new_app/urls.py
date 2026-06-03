from django.urls import path
from .views import task_create, task_list, task_detail, task_stats, \
SubTaskListCreateView, SubTaskDetailUpdateDeleteView

app_name = 'tasks'

urlpatterns = [
    path('task/create/', task_create, name='task-create'),
    path('task/', task_list, name='task-list'),
    path('task/<int:pk>/', task_detail, name='task-detail'),
    path('stats/', task_stats, name="task-stats"),
    path('subtasks/', SubTaskListCreateView.as_view(), name="subtask-list-create"),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name="subtask-detail-update-delete")
]