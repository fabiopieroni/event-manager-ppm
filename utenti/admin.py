from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registro utente personalizzato nel pannello admin
admin.site.register(CustomUser, UserAdmin)