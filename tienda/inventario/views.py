from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from .models import Producto
from .forms import productoForm
from django.views.generic import View,TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

# def index(request):
#     return HttpResponse("Hola mundo!")
# # Create your views here.

# def fecha(request):
#     fecha_actual = datetime.now()
#     return HttpResponse(fecha_actual)           

# def edad(request,nacimiento):
#     anio= datetime.now().year
#     edad=anio-nacimiento
#     return HttpResponse(edad)

# def nombre(request,nombre):
#     saludo='Hola, ¿Cómo estás? '+nombre
#     return HttpResponse(saludo)

# def datos(request,nombre,nacimiento):
#     anio= datetime.now().year
#     edad=anio-nacimiento
#     saludo='Hola, ¿Cómo estás? '+nombre+' tienes '+str(edad)+ ' años'
#     return redirect("inventario:home",saludo)

# def home(request,nombre):
#     if request.method == 'GET':
#         context={   'name':nombre,
#                     'lastname':'apellido'}
#         template=loader.get_template('inventario/home.html')
#         return HttpResponse(template.render(context,request))

# def ventas(request):
#     if request.method =='GET':
#         return render(request,'inventario/ventas.html')
 
# def productos(request):
#     if request.method == "POST":
#         producto = request.POST['txtproducto']
#         return redirect('inventario:ventas')
#     return render(request,'inventario/productos.html')

class claseIndex(View):
    def get(self, request):
        return render(request,'inventario/home.html')

class claseProductos(View):
    form_class = productoForm
    template_name='inventario/productos.html'
    def get(self, request):
        form =self.form_class(request.POST)
        context={'form': form}
        return render(request,self.template_name,context)
  
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            context={'form': form}
            return redirect('inventario:claseIndex')
        return render(request,self.template_name,context)

class homeTemplate(TemplateView):
    template_name = "inventario/home.html"

# class productoList(TemplateView):
#    template_name = "inventario/productos.html"

class productoCreate(CreateView):
  model=Producto
  template_name='inventario/productoCreate.html'
  form_class=productoForm
  success_url=reverse_lazy('inventario:productoList')

class productoList(ListView):
  model=Producto
  template_name='inventario/productos.html'
  form_class=productoForm

class productoUpdate(UpdateView):
    model=Producto
    template_name='inventario/productoUpdate.html'
    form_class=productoForm
    success_url = reverse_lazy('inventario:productoList')

class productoDelete(DeleteView):
   model=Producto
   context_object_name='producto'
   template_name='inventario/productoDelete.html'
   success_url=reverse_lazy('inventario:productoList')

