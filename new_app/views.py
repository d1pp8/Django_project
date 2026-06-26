from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Task, SubTask, Category
from . import serializers

from django.db.models import Count, Q
from django.utils import timezone


class TaskListCreateView(ListCreateAPIView):

    serializer_class = serializers.TaskListSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):

        queryset = Task.objects.all()

        status = self.request.query_params.get('status')
        deadline = self.request.query_params.get('deadline')
        search = self.request.query_params.get('search')
        ordering = self.request.query_params.get('ordering')


        if status:
            queryset = queryset.filter(status=status)
        if deadline:
            queryset = queryset.filter(deadline__date=deadline)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset



class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]



class SubTaskListCreateView(ListCreateAPIView):

    serializer_class = serializers.SubTaskSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):

        queryset = SubTask.objects.all()

        status = self.request.query_params.get('status')
        search = self.request.query_params.get('search')
        ordering = self.request.query_params.get('ordering')

        if status:
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

class SubTaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = serializers.SubTaskSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]




@api_view(['GET'])
@permission_classes([AllowAny])
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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        return Response({
            'category': category.name,
            'tasks': category.tasks.count()
        })

    def get_permissions(self):
        if self.action in ['list', 'retrieve','count_tasks']:
            return [AllowAny()]
        return [IsAuthenticated()]
