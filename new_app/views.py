from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskCreateSerializer, TaskListSerializer, TaskDetailSerializer


from django.db.models import Count, Q


@api_view(['POST'])
def task_create(request):
    task = TaskCreateSerializer(data=request.data)

    if task.is_valid():
        task.save()
        return Response(task.data, status=status.HTTP_201_CREATED)
    else:
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()

    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    serializer = TaskDetailSerializer(task)
    return Response(serializer.data)


@api_view(['GET'])
def task_stats(request):
    stats = Task.objects.aggregate(
        total_tasks=Count('id'),
        new_tasks=Count(
            'id',
            filter=Q(status='new')
        ),
        in_progress_tasks=Count(
            'id',
            filter=Q(status='in_progress')
        ),
        done_tasks=Count(
            'id',
            filter=Q(status='done')
        )
    )

    return Response(stats)