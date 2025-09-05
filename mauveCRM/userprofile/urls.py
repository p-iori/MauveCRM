from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path('meu-perfil/', views.perfil, name='perfil'),
    path('cadastrar/', signup, name='signup'),
]