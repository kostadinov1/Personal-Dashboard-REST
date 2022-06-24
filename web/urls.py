
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('web.accounts.urls')),
    path('core/', include('web.core.urls')),
    path('gym/', include('web.physical_activities.urls')),
    path('periodization/', include('web.periodization.urls')),
    path('nutrition/', include('web.nutrition.urls')),
    path('dieting/', include('web.dieting.urls')),

]
