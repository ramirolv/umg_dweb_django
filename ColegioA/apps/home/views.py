from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Usuario
from .forms import ArticuloForm, AutorizadorForm, ComentarioForm, EstudianteForm, RegistroForm


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EstudiantesView(CreateView):
    template_name='students.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:home')

class CrearView(CreateView):
    template_name = 'crearEstudiante.html'

class AdministradoresView(CreateView):
    template_name='admins.html'
    form_class = AutorizadorForm
    success_url = reverse_lazy('home:home')

class PublicacionesView(CreateView):
    template_name='publications.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:home')

class ComentariosView(CreateView):
    template_name='comments.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:home')

class AcercaView(TemplateView):
    template_name='about.html'


class RegistroUserView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:home')

class LoginView(LoginView):
    template_name = 'login.html'