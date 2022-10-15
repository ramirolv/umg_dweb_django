from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Usuario
from .forms import EstudianteForm, RegistroForm


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EstudiantesView(CreateView):
    template_name='students.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:home')

class CrearView(CreateView):
    template_name = 'crearEstudiante.html'

class AdministradoresView(TemplateView):
    template_name='admins.html'

class PublicacionesView(TemplateView):
    template_name='publications.html'

class ComentariosView(TemplateView):
    template_name='comments.html'

class AcercaView(TemplateView):
    template_name='about.html'


class RegistroUserView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:home')