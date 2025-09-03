from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile

from team.models import Team

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid: 
            User = form.save()
            Userprofile.objects.create(user=user)   

            team = Team.objects.create(nome='Nome do time', criado_por=request.user)    
            team.membros.add(request.user)
            team.save()            

            return redirect('/entrar/')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })

@login_required
def perfil(request):    
    team = Team.objects.filter(criado_por=request.user)[0]

    return render(request, 'userprofile/perfil.html', {
        'team': team
    })