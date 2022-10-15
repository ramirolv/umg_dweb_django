from django import forms
from .models import Estudiante, Curso, Telefono, Autorizador, Articulo, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'


class AutorizadorForm(forms.ModelForm):
    class Meta:
        model = Autorizador
        fields = '__all__'


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

