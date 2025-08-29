from django.urls import path

from . import views

urlpatterns = [
    path('', views.clients_lista, name='clients_lista'),
    path('<int:pk>/', views.sobre_client, name='sobre_client'),
    path('<int:pk>/deletar/', views.deletar_client, name='deletar_client'),
    path('novo-cliente/', views.criar_client, name='add_client'),
    path('<int:pk>/editar/', views.editar_client, name='editar_client'),
]
