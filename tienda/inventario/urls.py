from django.urls import path
from inventario.views import (claseIndex,
claseProductos,homeTemplate,
productoList,productoCreate,productoUpdate,productoDelete,
ventaList,ventaCreate,ventaUpdate,ventaDelete)

app_name='inventario'

urlpatterns = [
    path('claseIndex/',claseIndex.as_view(),name='claseIndex'),
    path('claseProductos/',claseProductos.as_view(),name='claseProductos'),
    path('homeTemplate/',homeTemplate.as_view(),name='homeTemplate'),  
    path('productoList/',productoList.as_view(),name='productoList'),
    path('productoCreate/',productoCreate.as_view(),name='productoCreate'),  
    path('productoUpdate/<int:pk>',productoUpdate.as_view(),name='productoUpdate'),
    path('productoDelete/<int:pk>',productoDelete.as_view(),name='productoDelete'),
    path('ventaList/',ventaList.as_view(),name='ventaList'),
    path('ventaCreate/',ventaCreate.as_view(),name='ventaCreate'),
    path('ventaUpdate/<int:pk>',ventaUpdate.as_view(),name='ventaUpdate'),
    path('ventaDelete/<int:pk>',ventaDelete.as_view(),name='ventaDelete'),
]