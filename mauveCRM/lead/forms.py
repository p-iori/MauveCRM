from django import forms 

from .models import Lead, Comment, LeadFile

class NovaLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('nome', 'email', 'sobre', 'prioridade', 'status',)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)