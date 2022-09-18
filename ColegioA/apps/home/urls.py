"""ColegioA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.home import views
from .views import HomeView, EstudiantesView, AdministradoresView, PublicacionesView, ComentariosView, AcercaView, CrearView

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('estudiantes/', EstudiantesView.as_view(), name='estudiantesapp'),
    path('admins/', AdministradoresView.as_view(), name='adminsapp'),
    path('publicaciones/', PublicacionesView.as_view(), name='publicationsapp'),
    path('comentarios/', ComentariosView.as_view(), name='commentsapp'),
    path('acerca/', AcercaView.as_view(), name='acercaapp'),
    path('crear/', CrearView.as_view(), name='crear'),
]
