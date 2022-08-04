from django.test import TestCase
from django.utils import timezone
from .models import Producto,Venta
# Create your tests here.
class ProductoModelTests(TestCase):
    def test_producto_create(self):
        producto=Producto.objects.create(
            nombre = "cereal",
            precioUnidad = "1",
            cantidadExistencia = "90",
            IVAproducto = "16",
        )
        assert producto.nombre == "cereal" 
class VentaModelTests(TestCase):
    def test_producto_create(self):
        venA=Venta.objects.create()
