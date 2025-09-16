from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy

from .forms import AddCommentForm, AddFileForm
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()

        return queryset.filter(criada_por=self.request.user, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['form'] = AddCommentForm()
            context['fileform'] = AddFileForm()

            return context

class LeadDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:lista')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()

        return queryset.filter(criada_por=self.request.user, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class LeadUpdateView(UpdateView):
    model = Lead
    fields = ('nome', 'email', 'sobre', 'prioridade', 'status',)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Informações'

        return context

    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()

        return queryset.filter(criada_por=self.request.user, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('leads:lista')

class LeadCreateView(CreateView):
    model = Lead
    fields = ('nome', 'email', 'sobre', 'prioridade', 'status',)
    success_url = reverse_lazy('leads:lista')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.filter(criado_por=self.request.user)[0]
        context['team'] = team
        context['title'] = 'Cadastrar lead'

        return context

    def form_valid(self, form):
        team = Team.objects.filter(criado_por=self.request.user)[0]

        self.object = form.save(commit=False)
        self.object.criada_por = self.request.user
        self.object.team = team
        self.object.save()

        return redirect(self.get_success_url())

class AddFileView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            team = Team.objects.filter(criado_por=self.request.user)[0]
            file = form.save(commit=False)
            file.team = team
            file.criado_por = request.user
            file.lead_id = pk
            file.save()

        return redirect('leads:sobre', pk=pk)

class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        form = AddCommentForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(criado_por=self.request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.criado_por = request.user
            comment.lead_id = pk
            comment.save()

        return redirect('leads:sobre', pk=pk)

class CovertToClientView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

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
