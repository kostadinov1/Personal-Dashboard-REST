from django.shortcuts import render
from rest_framework import generics as api_generic_views

from web.periodization.models import TimeCycle
from web.periodization.serializers import ListAllTimeCyclesSerializer, CreateTimeCycleSerializer, \
    EditTimeCycleSerializer, DeleteTimeCycleSerializer


class ListAllTimeCyclesView(api_generic_views.ListAPIView):
    queryset = TimeCycle.objects.all()
    serializer_class = ListAllTimeCyclesSerializer


class CreateTimeCycleView(api_generic_views.CreateAPIView):
    queryset = TimeCycle.objects.all()
    serializer_class = CreateTimeCycleSerializer


class EditTimeCycleView(api_generic_views.UpdateAPIView):
    queryset = TimeCycle.objects.all()
    serializer_class = EditTimeCycleSerializer

class DeleteTimeCycleView(api_generic_views.DestroyAPIView):
    queryset = TimeCycle.objects.all()
    serializer_class = DeleteTimeCycleSerializer