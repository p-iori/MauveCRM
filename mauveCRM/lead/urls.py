from django.urls import path

from . import views 

app_name = 'leads'

urlpatterns = [
    path('', views.LeadListView.as_view(), name='lista'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='sobre'),
    path('<int:pk>/deletar/', views.LeadDeleteView.as_view(), name='deletar'),
    path('<int:pk>/editar/', views.editar_lead, name='editar'),
    path('<int:pk>/converter/', views.converter_para_client, name='converter'),
    path('nova-lead/', views.criar_lead, name='add'),
]
