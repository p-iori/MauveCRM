from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path('<int:pk>/editar/', views.editar_team, name='editar'),
]

