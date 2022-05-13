from django.contrib import admin
from .models import Categoria, Contatos

class ContatosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 5
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable =  ('telefone', 'mostrar')
    

admin.site.register(Categoria)
admin.site.register(Contatos, ContatosAdmin)
