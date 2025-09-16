from django.contrib.auth.models import User
from django.db import models
from team.models import Team

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

    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    sobre = models.CharField(blank=True, null=True) 
    prioridade = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NOVO)
    convertida_para_client = models.BooleanField(default=False)
    criada_por = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)
    modificada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class LeadFile(models.Model):
    team = models.ForeignKey(Team, related_name='files', on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='empfiles')
    criado_por = models.ForeignKey(User, related_name='leads_files', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.criado_por.username

class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='lead_comments', on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    criado_por = models.ForeignKey(User, related_name='lead_comments', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.criado_por.username
    

