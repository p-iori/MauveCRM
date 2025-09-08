from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Lead

from client.models import Client
from team.models import Team

from .forms import NovaLeadForm


class LeadListView(ListView):
    model = Lead

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        queryset = queryset.filter(
            criada_por=self.request.user, convertida_para_client=False)

        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LeadDetailView(DetailView):
    model = Lead

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()

        return queryset.filter(criada_por=self.request.user, pk=self.kwargs.get('pk'))

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super().dispatch(*args, **kwargs)


@login_required
def editar_lead(request, pk):
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)

    if request.method == 'POST':
        form = NovaLeadForm(request.POST, instance=lead)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.save()

            messages.success(request, "Mudanças aplicadas com sucesso.")

            return redirect('leads:lista')
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
            team = Team.objects.filter(criado_por=request.user)[0]

            lead = form.save(commit=False)
            lead.criada_por = request.user
            lead.team = team
            lead.save()

            messages.success(request, "Lead criada.")

            return redirect('leads:lista')
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

    return redirect('leads:lista')


@login_required
def converter_para_client(request, pk):
    lead = Lead.objects.filter(criada_por=request.user).get(pk=pk)
    team = Team.objects.filter(criado_por=request.user)[0]

    client = Client.objects.create(
        nome=lead.nome,
        email=lead.email,
        sobre=lead.sobre,
        criado_por=request.user,
        team=team,
    )

    lead.convertida_para_client = True
    lead.save()

    messages.success(request, "Lead convertida para cliente.")

    return redirect('leads:lista')
