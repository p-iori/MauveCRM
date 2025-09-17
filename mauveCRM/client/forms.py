from django import forms 

from .models import Client, Comment, ClientFile

class NovoClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nome', 'email', 'sobre',)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = ClientFile
        fields = ('file',)