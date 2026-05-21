from django.contrib import admin
from django.db.models import F

from .models import Task, SubTask, Category


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    max_num = 10


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'show_title',
        'description',
        # 'category',
        'status',
        'created_at',
        'deadline'
    ]

    search_fields = [
        'title',
        'categories__name',
    ]

    list_filter = [
        'categories',
        'status',
        'deadline',
        'created_at'
    ]

    list_editable = [
        'status',
    ]

    inlines = [SubTaskInline]

    @admin.display(description="Title")
    def show_title(self, obj: Task) -> str:
        if len(obj.title) > 10:
            return obj.title[:10] + "..."
        else:
            return f"{obj.title}"


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'task',
        'status',
        'created_at',
        'deadline'
    ]

    search_fields = [
        'title',
        'task__title',
    ]

    list_filter = [
        'status',
        'deadline',
        'created_at'
    ]

    list_editable = [
        'status',
    ]

    actions = ['mark_sub_task_as_complete']

    @admin.action(description="Mark as done")
    def mark_sub_task_as_complete(self, request, sub_task):
        sub_task.update(status='dn')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]
