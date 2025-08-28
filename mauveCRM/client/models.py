from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    sobre = models.CharField(blank=True, null=True) 
    criada_por = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)
    modificada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome