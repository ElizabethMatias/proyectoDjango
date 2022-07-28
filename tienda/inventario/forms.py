from django import forms
from inventario.models import Producto
from django.db import models

class productoForm(forms.ModelForm):
  class Meta:
    model 	= Producto
    fields  =  '__all__' 