from django import forms
from inventario.models import Producto,Venta
from django.db import models

class productoForm(forms.ModelForm):
  class Meta:
    model 	= Producto
    fields  =  '__all__' 

class ventaForm(forms.ModelForm):
 class Meta:
   model   = Venta
   fields  = [ 'id_producto',
          'unidadesVendidas',
          'fecha',
          'tipoPago',
          'subTotal',
          'IVAtotal',
          'total',
   ]

