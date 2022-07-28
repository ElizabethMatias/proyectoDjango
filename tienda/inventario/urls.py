from django.urls import path
from inventario.views import (
    # index,fecha,edad,nombre,datos,home,productos,ventas,
    claseIndex,claseProductos,homeTemplate,productoList,productoCreate,productoUpdate,productoDelete

    )

app_name='inventario'

urlpatterns = [
    # #Empezar a importar las vistas
    # path('index/', index, name='index'),
    # path('fecha/', fecha, name='fecha'),
    # path('edad/<int:nacimiento>',edad, name='edad'),
    # path('nombre/<str:nombre>',nombre,name='nombre'),
    # path('datos/<str:nombre>/<int:nacimiento>',datos,name='datos'),
    # path('home/<str:nombre>',home,name='home'),
    # path('ventas/',ventas,name='ventas'),
    # path('productos/',productos,name='productos'),
    path('claseIndex/',claseIndex.as_view(),name='claseIndex'),
    path('claseProductos/',claseProductos.as_view(),name='claseProductos'),
    path('homeTemplate/',homeTemplate.as_view(),name='homeTemplate'),
    path('productoList/',productoList.as_view(),name='productoList'),
    path('productoCreate/',productoCreate.as_view(),name='productoCreate'),
    path('productoUpdate/<int:pk>',productoUpdate.as_view(),name='productoUpdate'),
    path('productoDelete/<int:pk>',productoDelete.as_view(),name='productoDelete'),
]