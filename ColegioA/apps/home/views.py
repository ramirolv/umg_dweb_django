from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Articulo, Autorizador, Comentario, Usuario, Estudiante
from .forms import ArticuloForm, AutorizadorForm, ComentarioForm, EstudianteForm, RegistroForm


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'


class EstudiantesView(CreateView, ListView):
    template_name='students.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:estudiantesapp')
    model = Estudiante

    def get_query(self):
        return Estudiante.objects.all()


class ListarEstudianteView(ListView):
    template_name = 'listarestudiante.html'
    model = Estudiante

    def get_query(self):
        return Estudiante.objects.all()


class CrearView(CreateView):
    template_name = 'crearEstudiante.html'


class AdministradoresView(CreateView, ListView):
    template_name='admins.html'
    form_class = AutorizadorForm
    success_url = reverse_lazy('home:adminsapp')
    model = Autorizador

    def get_query(self):
        return Autorizador.objects.all()


class PublicacionesView(CreateView, ListView):
    template_name='publications.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:publicationsapp')
    model = Articulo

    def get_query(self):
        return Articulo.objects.all()


class ComentariosView(CreateView, ListView):
    template_name='comments.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:home')
    model = Comentario

    def get_query(self):
        return Comentario.objects.all()


class AcercaView(TemplateView):
    template_name='about.html'


class RegistroUserView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:home')


class LoginView(LoginView):
    template_name = 'login.html'