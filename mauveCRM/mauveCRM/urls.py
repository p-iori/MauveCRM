from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clientes/', include('client.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    path('cadastrar/', signup, name='signup'),
    path('entrar/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('sair/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
