from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Lead


from .forms import NovaLeadForm

@login_required 
def leads_lista(request):
    leads = Lead.objects.filter(criada_por=request.user)
    return render(request, 'lead/leads_lista.html', {
        'leads': leads
    })

@login_required
def criar_lead(request):
    if request.method == 'POST':
        form = NovaLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.criada_por = request.user
            lead.save()

            return redirect('dashboard')
    else:
        form = NovaLeadForm()

    return render(request, 'lead/add_lead.html', {
        'form': form
    })