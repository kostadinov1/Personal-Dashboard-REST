from django.urls import path

from web.periodization.views import CreateMacroCycleView, ListAllMacroCyclesView, EditMacroCycleView, \
    DeleteMacroCycleView, ListAllMesoCyclesView, CreateMesoCycleView, EditMesoCycleView, DeleteMesoCycleView, \
    ListAllMicroCyclesView, CreateMicroCycleView, EditMicroCycleView, DeleteMicroCycleView

urlpatterns = (
    # MACRO
    path('all-macro-cycles/', ListAllMacroCyclesView.as_view(), name='all macro cycles'),
    path('create-macro-cycle/', CreateMacroCycleView.as_view(), name='create macro cycle'),
    path('edit-macro-cycle/', EditMacroCycleView.as_view(), name='edit macro cycle'),
    path('delete-macro-cycle/', DeleteMacroCycleView.as_view(), name='delete macro cycle'),
    # MESO
    path('all-meso-cycles/', ListAllMesoCyclesView.as_view(), name='all meso cycles'),
    path('create-meso-cycle/', CreateMesoCycleView.as_view(), name='create meso cycle'),
    path('edit-meso-cycle/', EditMesoCycleView.as_view(), name='edit meso cycle'),
    path('delete-meso-cycle/', DeleteMesoCycleView.as_view(), name='delete meso cycle'),
    # MICRO
    path('all-micro-cycles/', ListAllMicroCyclesView.as_view(), name='all micro cycles'),
    path('create-micro-cycle/', CreateMicroCycleView.as_view(), name='create micro cycle'),
    path('edit-micro-cycle/', EditMicroCycleView.as_view(), name='edit micro cycle'),
    path('delete-micro-cycle/', DeleteMicroCycleView.as_view(), name='delete micro cycle'),
)