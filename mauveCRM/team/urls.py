from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/editar/', views.editar_team, name='editar_team'),
]

