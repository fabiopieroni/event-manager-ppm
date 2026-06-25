from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_eventi, name='home_eventi'),
    path('evento/<int:evento_id>/iscriviti/', views.iscriviti_evento, name='iscriviti_evento'),
    path('i-miei-eventi/', views.miei_eventi, name='miei_eventi'),  # <--- CONTROLLA QUESTA RIGA!
]