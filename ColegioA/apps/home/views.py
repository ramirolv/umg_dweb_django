from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EstudiantesView(TemplateView):
    template_name='students.html'

class AdministradoresView(TemplateView):
    template_name='admins.html'

class PublicacionesView(TemplateView):
    template_name='publications.html'

class ComentariosView(TemplateView):
    template_name='comments.html'

class AcercaView(TemplateView):
    template_name='about.html'