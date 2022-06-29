from django.urls import path

from web.physical_activities.views import CreateExerciseView, EditExerciseView, DeleteExerciseView, EditActivityView, \
    DeleteActivityView, ListExercisesView, CreateActivityView, ListActivitiesView

urlpatterns = (
    path('create-exercise/', CreateExerciseView.as_view(), name='create exercise'),
    path('edit-exercise/<int:pk>/', EditExerciseView.as_view(), name='edit exercise'),
    path('detele-exercise/<int:pk>/', DeleteExerciseView.as_view(), name='delete view'),
    path('list-exercises/', ListExercisesView.as_view(), name='list exercises'),
    path('create-activity/', CreateActivityView.as_view(), name='create activity'),
    path('edit-activity/<int:pk>/', EditActivityView.as_view(), name='edit activity'),
    path('delete-activity/<int:pk>/', DeleteActivityView.as_view(), name='delete activity'),
    path('list-activities/', ListActivitiesView.as_view(), name='list activities'),

)