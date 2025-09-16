from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.clients_lista, name='lista'),
    path('<int:pk>/', views.sobre_client, name='sobre'),
    path('<int:pk>/deletar/', views.deletar_client, name='deletar'),
    path('novo-cliente/', views.criar_client, name='add'),
    path('<int:pk>/novo-comentario/', views.sobre_client, name='add_comment'),
    path('<int:pk>/editar/', views.editar_client, name='editar'),
]
