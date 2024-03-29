from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import ObtainAuthToken

from core.views import home, user_login, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    path('login/verify', user_login, name="user_login_verify"),
    path('logout/', logout_view, name='logout'),
    path('', home),
    path('ecopontos/', include('ecopontos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('descartadores/', include('descartadores.urls')),
    path('descartes/', include('descartes.urls')),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
]
