from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TeamForm
from .models import Team

@login_required
def editar_team(request, pk):
    team = get_object_or_404(Team, criado_por=request.user, pk=pk)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()

            messages.success(request, "Time editado com sucesso.")
            return redirect('perfil')

    else:
        form = TeamForm(instance=team)

    return render(request, 'team/editar_team.html', {
        'team': team,
        'form': form
    })