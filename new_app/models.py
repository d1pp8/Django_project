from django.db import models

STATUS_OF_TASKS = [
    ('new', 'New'),
    ('in prog', 'In Progress'),
    ('pend', 'Pending'),
    ('bl', 'Blocked'),
    ('dn', 'Done'),
    ('na', 'N/A')
]


class Task(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )

    description = models.TextField()
    categories = models.ManyToManyField(
        'Category',
        related_name='tasks',
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_OF_TASKS,
        default='na'
    )

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at', 'title']


class SubTask(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )

    description = models.TextField()

    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name='subtasks'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_OF_TASKS,
        default='na'
    )

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at', 'title']

        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'