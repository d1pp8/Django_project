from django.urls import path
from .views import task_create, task_list, task_detail, task_stats

app_name = 'tasks'

urlpatterns = [
    path('create/', task_create, name='task-create'),
    path('list/', task_list, name='task-list'),
    path('<int:pk>/', task_detail, name='task-detail'),
    path('stats/', task_stats, name="task-stats")
]