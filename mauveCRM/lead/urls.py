from django.urls import path

from . import views 

urlpatterns = [
    path('', views.leads_lista, name='leads_lista'),
    path('<int:pk>/', views.sobre_lead, name='sobre_lead'),
    path('<int:pk>/deletar/', views.deletar_lead, name='deletar_lead'),
    path('<int:pk>/editar/', views.editar_lead, name='editar_lead'),
    path('<int:pk>/converter/', views.converter_para_client, name='converter_lead'),
    path('nova-lead/', views.criar_lead, name='add_lead'),
]
