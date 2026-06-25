from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utenti/', include('utenti.urls')), 
    path('', include('eventi.urls')),
]