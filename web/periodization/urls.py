from django.urls import path

from web.periodization.views import ListAllTimeCyclesView, DeleteTimeCycleView, EditTimeCycleView, CreateTimeCycleView

urlpatterns = (
    path('all-time-cycles/', ListAllTimeCyclesView.as_view(), name='all time cycles'),
    path('create-time-cycle/', CreateTimeCycleView.as_view(), name='create time cycle'),
    path('edit-time-cycle/', EditTimeCycleView.as_view(), name='edit time cycle'),
    path('delete-time-cycle/', DeleteTimeCycleView.as_view(), name='delete time cycle'),

)