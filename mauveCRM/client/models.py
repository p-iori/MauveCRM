from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    sobre = models.CharField(blank=True, null=True) 
    criado_por = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome