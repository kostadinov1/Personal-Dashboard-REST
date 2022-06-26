from rest_framework import generics as api_generic_views

from web.physical_activities.models import Exercise, Activity
from web.physical_activities.serializers import CreateExerciseSerializer, ListExercisesSerializer, \
    CreateActivitySerializer, ListActivitiesSerializer


class CreateExerciseView(api_generic_views.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = CreateExerciseSerializer


class ListExercisesView(api_generic_views.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ListExercisesSerializer


class CreateActivityView(api_generic_views.CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = CreateActivitySerializer


class ListActivitiesView(api_generic_views.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ListActivitiesSerializer
