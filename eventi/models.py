from django.db import models
from django.conf import settings

class Evento(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField()
    data_ora = models.DateTimeField()
    luogo = models.CharField(max_length=200)
    organizzatore = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='eventi_creati'
    )
    capienza_massima = models.PositiveIntegerField()

    def __str__(self):
        return self.titolo

    def posti_disponibili(self):
        iscriti = self.iscrizioni.count()
        return max(0, self.capienza_massima - iscriti)


class Iscrizione(models.Model):
    utente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='iscrizioni'
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='iscrizioni'
    )
    data_iscrizione = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Impedisce a un utente di iscriversi due volte allo stesso evento
        unique_together = ('utente', 'evento')

    def __str__(self):
        return f"{self.utente.username} -> {self.evento.titolo}"