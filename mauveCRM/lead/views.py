from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Lead

from client.models import Client

from .forms import NovaLeadForm

@login_required 
def leads_lista(request):
    leads = Lead.objects.filter(criada_por=request.user, convertida_para_client=False)
    return render(request, 'lead/leads_lista.html', {
        'leads': leads
    })

@login_required
def sobre_lead(request, pk): 
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)

    return render(request, 'lead/sobre_lead.html', {
        'lead': lead
    })

@login_required
def editar_lead(request, pk): 
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)

    if request.method == 'POST':
        form = NovaLeadForm(request.POST, instance=lead)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()

            messages.success(request, "Mudanças aplicadas com sucesso.")

            return redirect('leads_lista')
    else:
        form = NovaLeadForm(instance=lead)

    return render(request, 'lead/editar_leads.html', {
        'form': form
    })

@login_required
def criar_lead(request):
    if request.method == 'POST':
        form = NovaLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.criada_por = request.user
            lead.save()

            messages.success(request, "Lead criada.")


            return redirect('leads_lista')
    else:
        form = NovaLeadForm()

    return render(request, 'lead/add_lead.html', {
        'form': form
    })

@login_required
def deletar_lead(request, pk):
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)
    lead.delete()

    messages.success(request, "Lead deletada.")

    return redirect('leads_lista')

@login_required
def converter_para_client(request, pk):
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)

    client = Client.objects.create(
        nome=lead.nome,
        email=lead.email,
        sobre=lead.sobre,
        criada_por=request.user,
    )

    lead.convertida_para_client = True
    lead.save()

    messages.success(request, "Lead convertida para cliente.")

    return redirect('leads_lista')