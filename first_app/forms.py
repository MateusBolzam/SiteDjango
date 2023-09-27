from django import forms
from first_app.models import Personagem

class FormSimples(forms.Form):
    nome = forms.CharField(max_length=128)
    sobrenome = forms.CharField(max_length=128)
    email = forms.EmailField()
   
class FormPersona(forms.ModelForm):
    
    class Meta:
        model = Personagem
        fields = "__all__"
        
        #nao sei oq dizer
        
    
    