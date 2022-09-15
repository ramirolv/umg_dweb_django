from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)



class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s' % (self.nombre)


class Telefono(models.Model):
    tipo_telefono=(
        ('C', 'Casa'),
        ('M', 'Celular'),
        ('T', 'Trabajo'),
    )
    telefono = models.CharField(max_length=13)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=1,
        choices=tipo_telefono, 
        default='C',
        )
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.telefono)

class Autorizador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(Autorizador, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.descripcion, self.estudiante, self.autorizador)

class Comentario(models.Model):
    descripcion = models.CharField(max_length=250)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.descripcion, self.estudiante)