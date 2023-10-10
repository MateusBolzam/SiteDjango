from django.contrib import admin
from .models import Topico,Pagina,Acessos,Personagem,Peneira,Evento
# Register your models here.



class PersonagemAdmin(admin.ModelAdmin):
    
    fields = ['classe','nome','atributo']
    search_fields = ['classe','nome']
    list_filter = ['classe']
    


admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(Acessos)
admin.site.register(Peneira)
admin.site.register(Evento)
admin.site.register(Personagem,PersonagemAdmin)