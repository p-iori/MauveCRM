from django.urls import path

from . import views 

app_name = 'leads'

urlpatterns = [
    path('', views.LeadListView.as_view(), name='lista'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='sobre'),
    path('<int:pk>/deletar/', views.LeadDeleteView.as_view(), name='deletar'),
    path('<int:pk>/editar/', views.LeadUpdateView.as_view(), name='editar'),
    path('<int:pk>/converter/', views.CovertToClientView.as_view(), name='converter'),
    path('<int:pk>/novo-comentario/', views.AddCommentView.as_view(), name='add_comment'),
    path('nova-lead/', views.LeadCreateView.as_view(), name='add'),
]
