from django import forms 

from .models import Client, Comment 

class NovoClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nome', 'email', 'sobre',)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)