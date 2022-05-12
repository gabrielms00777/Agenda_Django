from django.shortcuts import render
from .models import Contatos

def index(request):
    contatos = Contatos.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    contato = Contatos.objects.get(id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
