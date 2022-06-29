from django.shortcuts import render
from rest_framework import generics as api_generic_views



class CreatePeriodizationView(api_generic_views.CreateAPIView):
    pass


class EditPeriodizationView(api_generic_views.UpdateAPIView):
    pass


class DeletePeriodization(api_generic_views.DestroyAPIView):
    pass
