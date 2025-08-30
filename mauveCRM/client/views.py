from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect 

from .forms import NovoClientForm

from .models import Client
from team.models import Team

@login_required
def clients_lista(request):
    clients = Client.objects.filter(criado_por=request.user)

    return render(request, 'client/clients_lista.html', {
        'clients': clients
})

@login_required
def sobre_client(request, pk):
    client = get_object_or_404(Client, criado_por=request.user, pk=pk)

    return render(request, 'client/sobre_client.html', {
        'client': client
})

@login_required
def criar_client(request):
    if request.method == 'POST':
        form = NovoClientForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(criado_por=request.user)[0]
            client = form.save(commit=False)
            client.criado_por = request.user
            client.team = team
            client.save()

            messages.success(request, "Client criado.")


            return redirect('clients_lista')
    else:
        form = NovoClientForm()

    return render(request, 'client/add_client.html', {
        'form': form
    })

@login_required
def deletar_client(request, pk):
    client = Client.objects.filter(criado_por=request.user).get(pk=pk)
    client.delete()

    messages.success(request, "Cliente deletado.")

    return redirect('clients_lista')

@login_required
def editar_client(request, pk): 
    client = Client.objects.filter(criado_por=request.user).get(pk=pk)

    if request.method == 'POST':
        form = NovoClientForm(request.POST, instance=client)

        if form.is_valid():
            client = form.save(commit=False)
            client.save()

            messages.success(request, "Mudanças aplicadas com sucesso.")

            return redirect('clients_lista')
    else:
        form = NovoClientForm(instance=client)

    return render(request, 'client/editar_client.html', {
        'form': form
    })
