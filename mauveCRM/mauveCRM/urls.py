from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from core.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clientes/', include('client.urls')),
    path('dashboard/times/', include('team.urls')),
    path('dashboard/', include('userprofile.urls')),  
    path('dashboard/', include('dashboard.urls')),  
    path('about/', about, name='about'),
    path('entrar/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('sair/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)