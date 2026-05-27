from django.urls import path
from .views import task_create

app_name = 'tasks'

urlpatterns = [
    path('create/', task_create, name='task-create')
]