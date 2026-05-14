from django.db import models
from unicodedata import category


STAUS_OF_TASKS = [
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
        unique_for_date='created_at',
        null=False,
        blank=False
    )

    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')

    status = models.CharField(
        max_length=10,
        choices=STAUS_OF_TASKS,
        default='na'
    )

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Subtask(models.Model):

    title = models.CharField(
        max_length=255,
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
        choices=STAUS_OF_TASKS,
        default='na'
    )

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=30)