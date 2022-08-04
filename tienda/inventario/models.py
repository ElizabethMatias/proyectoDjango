from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precioUnidad = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    cantidadExistencia = models.IntegerField(default=0)
    IVAproducto = models.DecimalField(default=0, max_digits=7, decimal_places=2)

#aplicacion de inventario
#Registramos en Views.py 
    #from .models import Producto
#python mmanage.py makemigrations inventario
#python mmanage.py migrate inventario
#registrar en admin.py
    #from .models import Producto
    #admin.site.register(Producto)

class Venta(models.Model):
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE,null=False,blank=False,default=1)
    unidadesVendidas = models.IntegerField(default=1)
    fecha = models.DateTimeField('fecha de venta')
    CHOICE = (
        ('EF', 'Efectivo'),
        ('TA', 'Tarjeta'),
    )
    tipoPago = models.CharField(
        choices = CHOICE,
        default = 'EF',
        max_length=200,
    )
    subTotal = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    vendedor = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,default=1)
    IVAtotal = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=7, decimal_places=2)