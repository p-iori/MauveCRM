from django import forms 

from .models import Lead 

class NovaLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('nome', 'email', 'sobre', 'prioridade', 'status',)