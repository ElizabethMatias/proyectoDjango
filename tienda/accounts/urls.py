from django.urls import path
from accounts.views import homeTemplate, login, registro, usuarioDelete,usuarioUpdate,usuarioDetail
from django.contrib.auth.views import LogoutView
app_name='accounts'

urlpatterns = [
    path('home/',homeTemplate.as_view(),name='homeTemplate'),  
    path('login/',login.as_view(),name='login'), 
    path('registro/',registro.as_view(),name='registro'), 
    path('logout/',LogoutView.as_view(),name='logout'),
    path('usuarioUpdate/<int:pk>',usuarioUpdate.as_view(),name='usuarioUpdate'),
    path('usuarioDetail/<int:pk>',usuarioDetail.as_view(),name='usuarioDetail'),
    path('usuarioDelete/<int:pk>',usuarioDelete.as_view(),name='usuarioDelete'),
]