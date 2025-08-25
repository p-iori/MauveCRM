from django.urls import path

from . import views 

urlpatterns = [
    path('nova-lead/', views.criar_lead, name='add_lead'),
]
