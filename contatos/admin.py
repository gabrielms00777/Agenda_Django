from django.contrib import admin
from .models import Categoria, Contatos

class ContatosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 5
    search_fields = ('nome', 'sobrenome', 'telefone')
    

admin.site.register(Categoria)
admin.site.register(Contatos, ContatosAdmin)
