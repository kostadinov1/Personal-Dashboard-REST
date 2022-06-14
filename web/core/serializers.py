from rest_framework import serializers

from web.core.models import ToDo, ToDoCategory


class ToDoForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class CategoryForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoCategory
        fields = ('id', 'name')
