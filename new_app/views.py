from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Task, SubTask, Category
import serializers


from django.db.models import Count, Q, Model
from django.utils import timezone


@api_view(['POST'])
def task_create(request):
    task = serializers.TaskCreateSerializer(data=request.data)

    if task.is_valid():
        task.save()
        return Response(task.data, status=status.HTTP_201_CREATED)
    else:
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()

    serializer = serializers.TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    serializer = serializers.TaskDetailSerializer(task)
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
        ),
        overdue_tasks=Count(
            'id',
            filter=Q(deadline__lt=timezone.now()) & ~Q(status='done')
        )
    )

    return Response(stats)


class SubTaskListCreateView(APIView):
    def get(self,request):
        subtasks = SubTask.objects.all()

        serializer = serializers.SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SubTaskCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        serializer = serializers.SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        serializer = serializers.SubTaskSerializer(subtask)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        subtask.delete()
        return Response(status=status.HTTP_200_OK)