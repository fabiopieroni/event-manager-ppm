from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_eventi, name='home_eventi'),
    path('evento/<int:evento_id>/iscriviti/', views.iscriviti_evento, name='iscriviti_evento'),
    path('evento/<int:evento_id>/disiscriviti/', views.disiscriviti_evento, name='disiscriviti_evento'),
    path('i-miei-eventi/', views.miei_eventi, name='miei_eventi'),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name='dettaglio_evento'),
    path('crea-evento/', views.crea_evento, name='crea_evento'),
    path('evento/<int:evento_id>/modifica/', views.modifica_evento, name='modifica_evento'),
    path('evento/<int:evento_id>/elimina/', views.elimina_evento, name='elimina_evento'),
]