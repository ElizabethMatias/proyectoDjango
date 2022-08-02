from django.urls import path
from accounts.views import homeTemplate, login

app_name='accounts'

urlpatterns = [
    path('home/',homeTemplate.as_view(),name='homeTemplate'),  
    path('login/',login.as_view(),name='login'), 
]