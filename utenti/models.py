from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('attendee', 'Attendee (Partecipante)'),
        ('organizer', 'Organizer (Organizzatore)'),
    )
    
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='attendee'
    )

    def is_organizer(self):
        return self.role == 'organizer' or self.is_superuser

    def is_attendee(self):
        return self.role == 'attendee' or self.is_superuser