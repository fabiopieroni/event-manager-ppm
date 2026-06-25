from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, Iscrizione

def home_eventi(request):
    eventi = Evento.objects.all().order_by('data_ora')
    return render(request, 'eventi/elenco_eventi.html', {'eventi': eventi})

@login_required
def iscriviti_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if not request.user.is_superuser and evento.posti_disponibili() > 0:
        Iscrizione.objects.get_or_create(utente=request.user, evento=evento)
        
    return redirect('home_eventi')

@login_required
def miei_eventi(request):
    iscrizioni = Iscrizione.objects.filter(utente=request.user).select_related('evento')
    return render(request, 'eventi/miei_eventi.html', {'iscrizioni': iscrizioni})