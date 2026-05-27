from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskCreateSerializer

from django.http import HttpResponse, HttpRequest


def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")


@api_view(['POST'])
def task_create(request):
    task = TaskCreateSerializer(data=request.data)

    if task.is_valid():
        task.save()
        return Response(task.data, status=status.HTTP_201_CREATED)
    else:
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)
