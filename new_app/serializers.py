from rest_framework import serializers
from django.utils import timezone
from .models import Task, SubTask, Category

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'deadline'
        ]

    def validate_deadline(self, deadline):
        if deadline < timezone.now():
            raise serializers.ValidationError("The deadline must be later than the current time.")
        return deadline

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status'
        ]

class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError({"name": "Category already exists"})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exclude(id=instance.id).exclude():
            raise serializers.ValidationError({"name": "Category already exists"})
        return super().update(instance,validated_data)



class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskCreateSerializer(many=True,read_only=True)

    class Meta:
        model = Task
        fields = '__all__'