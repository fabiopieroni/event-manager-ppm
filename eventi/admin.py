from django.contrib import admin
from .models import Evento, Iscrizione

# Registro le tabelle per poterle gestire dal sito
admin.site.register(Evento)
admin.site.register(Iscrizione)