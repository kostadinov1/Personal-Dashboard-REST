from django.shortcuts import render
from rest_framework import generics as api_views

from web.core.models import ToDo, ToDoCategory
from web.core.serializers import ToDoForListSerializer, CategoryForListSerializer


class CreateToDoView(api_views.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoForListSerializer

    def get_queryset(self):
        qs = super(CreateToDoView, self).get_queryset()
        # filter is not mutating, so it needs to be saved in the var again
        qs = qs.filter(user=self.request.user)

        # TODO swap it with mixin when client is made to be able to test it properly
        category_id = self.request.query_params.get('category', None)
        if category_id:
            qs = qs.filter(category_id=category_id)

        return qs


class ListToDosView(api_views.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoForListSerializer


class CreateToDoCategoryView(api_views.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = CategoryForListSerializer


class ListToDoCategoriesView(api_views.ListAPIView):
    queryset = ToDoCategory.objects.all()
    serializer_class = CategoryForListSerializer


