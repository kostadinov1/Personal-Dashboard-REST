from django.urls import path

from web.physical_activities.views import CreateExerciseView

urlpatterns = (
    path('create-exercise/', CreateExerciseView.as_view(), name='create exercise'),
    path('edit-exercise/', EditExerciseView.as_view(), name='edit exercise'),
    path('list-exercises/', CreateExerciseView.as_view(), name='list exercises'),
    path('create-activity/', CreateExerciseView.as_view(), name='create activity'),
    path('list-activities/', CreateExerciseView.as_view(), name='list activities'),

)