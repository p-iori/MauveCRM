from django.urls import path

from . import views 

urlpatterns = [
    path('', views.leads_lista, name='leads_lista'),
    path('<int:pk>/', views.sobre_lead, name='sobre_lead'),
    path('nova-lead/', views.criar_lead, name='add_lead'),
]
