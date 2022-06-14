from django.urls import path

from web.core.views import CreateToDoView, ListToDosView, ListToDoCategoriesView, CreateToDoCategoryView

urlpatterns = (
    path('create-todo/', CreateToDoView.as_view(), name='create todo'),
    path('list-todos/', ListToDosView.as_view(), name='list todos'),
    path('create-category/', CreateToDoCategoryView.as_view(), name='create todo category'),
    path('categories/', ListToDoCategoriesView.as_view(), name='list todo categories'),

)