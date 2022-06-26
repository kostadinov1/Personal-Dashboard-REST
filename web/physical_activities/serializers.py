from rest_framework import serializers

from web.physical_activities.models import Exercise, Activity


class CreateExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class ListExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class CreateActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ListActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
