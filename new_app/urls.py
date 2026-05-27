from django.urls import path
from .views import task_create, task_list, task_detail

app_name = 'tasks'

urlpatterns = [
    path('create/', task_create, name='task-create'),
    path('list/', task_list, name='task-list'),
    path('<int:pk>/', task_detail, name='task-detail'),
]