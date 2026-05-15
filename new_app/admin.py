from django.contrib import admin

from .models import Task, SubTask, Category




class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
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

class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
admin.site.register(Category, CategoryAdmin)