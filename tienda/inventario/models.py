from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precioUnidad = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    cantidadExistencia = models.IntegerField(default=0)
    IVAproducto = models.DecimalField(default=0, max_digits=7, decimal_places=2)


class Venta(models.Model):
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
    vendedor = models.CharField(max_length=200)
    IVAtotal = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=7, decimal_places=2)

class VentaProducto(models.Model):
    unidadesTotales = models.IntegerField(default=1)
    precioUnidades = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    IVAtotal = models.DecimalField(default=0,max_digits=7, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)