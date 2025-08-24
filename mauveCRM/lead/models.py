from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    LOW = 'baixa'
    MEDIUM = 'media'
    HIGH = 'alta'

    CHOICES_PRIORITY = {
        (LOW, 'Baixa'),
        (MEDIUM, 'Média'),
        (HIGH, 'Alta')
    }

    NEW = 'novo'
    CONTACTED = 'contactado'
    WON = 'convertida'
    LOST = 'perdida'

    CHOICES_STATUS = {
        (NEW, 'Novo'),
        (CONTACTED, 'Contactado'),
        (WON, 'Convertida'),
        (LOST, 'Perdida'),
    }

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(blank=True, null=True) 
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name