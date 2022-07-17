from django.shortcuts import render
from rest_framework import generics as api_generic_views

from web.periodization.models import MacroCycle, MesoCycle, MicroCycle
from web.periodization.serializers import ListAllMacroCyclesSerializer, CreateMacroCycleSerializer, \
    EditMacroCycleSerializer, DeleteMacroCycleSerializer, ListAllMesoCyclesSerializer, CreateMesoCycleSerializer, \
    EditMesoCycleSerializer, DeleteMesoCycleSerializer, ListAllMicroCyclesSerializer, CreateMicroCycleSerializer, \
    EditMicroCycleSerializer, DeleteMicroCycleSerializer


class ListAllMacroCyclesView(api_generic_views.ListAPIView):
    queryset = MacroCycle.objects.all()
    serializer_class = ListAllMacroCyclesSerializer


class CreateMacroCycleView(api_generic_views.CreateAPIView):
    queryset = MacroCycle.objects.all()
    serializer_class = CreateMacroCycleSerializer


class EditMacroCycleView(api_generic_views.UpdateAPIView):
    queryset = MacroCycle.objects.all()
    serializer_class = EditMacroCycleSerializer


class DeleteMacroCycleView(api_generic_views.DestroyAPIView):
    queryset = MacroCycle.objects.all()
    serializer_class = DeleteMacroCycleSerializer

# ======================================   MESO CYCLES   =============================== #


class ListAllMesoCyclesView(api_generic_views.ListAPIView):
    queryset = MesoCycle.objects.all()
    serializer_class = ListAllMesoCyclesSerializer


class CreateMesoCycleView(api_generic_views.CreateAPIView):
    queryset = MesoCycle.objects.all()
    serializer_class = CreateMesoCycleSerializer


class EditMesoCycleView(api_generic_views.UpdateAPIView):
    queryset = MesoCycle.objects.all()
    serializer_class = EditMesoCycleSerializer


class DeleteMesoCycleView(api_generic_views.DestroyAPIView):
    queryset = MesoCycle.objects.all()
    serializer_class = DeleteMesoCycleSerializer

# ======================================   MICRO CYCLES   =============================== #

class ListAllMicroCyclesView(api_generic_views.ListAPIView):
    queryset = MicroCycle.objects.all()
    serializer_class = ListAllMicroCyclesSerializer


class CreateMicroCycleView(api_generic_views.CreateAPIView):
    queryset = MicroCycle.objects.all()
    serializer_class = CreateMicroCycleSerializer


class EditMicroCycleView(api_generic_views.UpdateAPIView):
    queryset = MicroCycle.objects.all()
    serializer_class = EditMicroCycleSerializer


class DeleteMicroCycleView(api_generic_views.DestroyAPIView):
    queryset = MicroCycle.objects.all()
    serializer_class = DeleteMicroCycleSerializer

