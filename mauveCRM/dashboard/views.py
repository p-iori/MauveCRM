from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from lead.models import Lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    
    leads = Lead.objects.filter(team=team, convertida_para_client=False).order_by('-criada_em')[0:5]
    clients = Client.objects.filter(team=team).order_by('-criado_em')[0:5]
    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })