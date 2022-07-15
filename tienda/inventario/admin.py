from django.contrib import admin

# Register your models here.
from .models import Producto, VentaProducto, Venta

admin.site.register(Producto)
admin.site.register(VentaProducto)
admin.site.register(Venta)