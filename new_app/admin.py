from django.contrib import admin

from .models import Task, Subtask, Category

admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Category)