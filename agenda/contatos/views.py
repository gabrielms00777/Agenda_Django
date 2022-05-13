from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contatos

def index(request):
    contatos = Contatos.objects.all()
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    #contato = Contatos.objects.get(id=contato_id)
    contato = get_object_or_404(Contatos, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })