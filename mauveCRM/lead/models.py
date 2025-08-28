from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    LOW = 'baixa'
    MEDIUM = 'media'
    HIGH = 'alta'

    CHOICES_PRIORITY = [
        (LOW, 'Baixa'),
        (MEDIUM, 'Média'),
        (HIGH, 'Alta')
    ]

    NOVO = 'novo'
    CONT = 'contactada'
    CONV = 'convertida'
    PERD = 'perdida'

    CHOICES_STATUS = [
        (NOVO, 'Novo'),
        (CONT, 'Contactada'),
        (CONV, 'Convertida'),
        (PERD, 'Perdida'),
    ]

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    sobre = models.CharField(blank=True, null=True) 
    prioridade = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NOVO)
    convertida_para_client = models.BooleanField(default=False)
    criada_por = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)
    modificada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome