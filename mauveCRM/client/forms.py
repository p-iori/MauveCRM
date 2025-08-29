from django import forms 

from .models import Client 

class NovoClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nome', 'email', 'sobre',)