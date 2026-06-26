from .forms import EventoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Evento, Iscrizione

def home_eventi(request):
    eventi = Evento.objects.all().order_by('data_ora')
    iscrizioni_utente = []
    if request.user.is_authenticated:
        iscrizioni_utente = Iscrizione.objects.filter(utente=request.user).values_list('evento_id', flat=True)
    return render(request, 'eventi/elenco_eventi.html', {
        'eventi': eventi, 
        'iscrizioni_utente': iscrizioni_utente
    })

@login_required
def iscriviti_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if not request.user.is_superuser and evento.posti_disponibili() > 0:
        Iscrizione.objects.get_or_create(utente=request.user, evento=evento)
    return redirect('home_eventi')

@login_required
def disiscriviti_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    Iscrizione.objects.filter(utente=request.user, evento=evento).delete()
    return redirect(request.META.get('HTTP_REFERER', 'home_eventi'))

@login_required
def miei_eventi(request):
    iscrizioni = Iscrizione.objects.filter(utente=request.user).select_related('evento')
    return render(request, 'eventi/miei_eventi.html', {'iscrizioni': iscrizioni})

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'eventi/dettaglio_evento.html'
    context_object_name = 'evento'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['iscritti'] = Iscrizione.objects.filter(evento=self.object).select_related('utente')
        return context

@login_required
def crea_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            nuovo_evento = form.save(commit=False)
            nuovo_evento.organizzatore = request.user
            nuovo_evento.save()
            return redirect('home_eventi')
    else:
        form = EventoForm()

    return render(request, 'eventi/crea_evento.html', {'form': form})    

@login_required
def modifica_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if evento.organizzatore != request.user and not request.user.is_superuser:
        return render(request, 'eventi/errore_permessi.html', status=403)
        
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('dettaglio_evento', pk=evento.id)
    else:
        form = EventoForm(instance=evento)
        
    return render(request, 'eventi/crea_evento.html', {'form': form, 'modifica': True})

@login_required
def elimina_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if evento.organizzatore != request.user and not request.user.is_superuser:
        return render(request, 'eventi/errore_permessi.html', status=403)
        
    if request.method == 'POST':
        evento.delete()
        return redirect('home_eventi')
        
    return render(request, 'eventi/conferma_elimina.html', {'evento': evento})