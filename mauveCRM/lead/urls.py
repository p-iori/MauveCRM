from django.urls import path

from . import views 

app_name = 'leads'

urlpatterns = [
    path('', views.leads_lista, name='lista'),
    path('<int:pk>/', views.sobre_lead, name='sobre'),
    path('<int:pk>/deletar/', views.deletar_lead, name='deletar'),
    path('<int:pk>/editar/', views.editar_lead, name='editar'),
    path('<int:pk>/converter/', views.converter_para_client, name='converter'),
    path('nova-lead/', views.criar_lead, name='add'),
]
