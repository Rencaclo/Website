from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TipoObras(models.Model):
    tecnica = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.tecnica


class Producto(models.Model):
    codigo_producto = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    historia = models.CharField(max_length=100)
    imagen = CloudinaryField('imagen')
    tecnica = models.ForeignKey(TipoObras, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.nombre
    


class usuario(models.Model):
    rut = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    correo = models.EmailField(max_length=50)
    solicitud = models.BooleanField(default=False)
    tipo_id = models.BigIntegerField()


class Carrito(models.Model):
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    imagen = models.ImageField(upload_to= "carrito", null=False)
    usuario_producto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cantidad} of {self.nombre_producto}"

    
