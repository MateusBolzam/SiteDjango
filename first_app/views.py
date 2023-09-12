from django.shortcuts import render

from first_app.models import Topico,Pagina,Acessos

from . import forms
from .forms import FormSimples,FormPersona



# Create your views here.


def index(request):
    
    return render(request, 'Aula1.html')

def math(request):
    
    return render(request, 'Calculadora.html')

def table(request):
    
    lista = {"lista_acessos": Acessos.objects.order_by('date')}
    
    return render(request, 'Table.html', lista)

def formulario_simples(request):
    form = forms.FormSimples()
    
    if request.method == 'POST':
        
        form = forms.FormSimples(request.POST)
        
        if form.is_valid():
            
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['nome'])
            print("Name"+form.cleaned_data['sobrenome'])
            print("Name"+form.cleaned_data['email'])
    
    
    return render(request, 'form_simples.html', context={'form': form})

def personagem(request):
    form = FormPersona()
    
    if request.method == "POST":
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Erro")
            
    return render(request, 'formPersona.html',{'form':form})