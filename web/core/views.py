from django.shortcuts import render
from rest_framework import generics as api_views


class CreateToDoView(api_views.ListCreateAPIView):
    pass