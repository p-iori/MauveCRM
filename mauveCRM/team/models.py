from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(User, related_name='teams')
    criado_por = models.ForeignKey(User, related_name='teams_criados', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
