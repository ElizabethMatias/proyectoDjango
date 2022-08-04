from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import Usuario
# Create your views here.
class homeTemplate(TemplateView):
   template_name = "accounts/home.html"

class login(LoginView):
   template_name = "accounts/login.html"

class registro(CreateView):
   model=User
   template_name = "accounts/registro.html"
   form_class=Usuario
   success_url=reverse_lazy("accounts:login")

class usuarioUpdate(UpdateView):
   model=User
   template_name = "accounts/userUpdate.html"
   fields=('username',
            'first_name',
            'last_name',
            'email',)
   success_url=reverse_lazy("inventario:homeTemplate")

class usuarioDetail(DetailView):
   model=User
   template_name = "accounts/userDetail.html"

class usuarioDelete(DeleteView):
   model=User
   template_name="accounts/userDelete.html"
   context_object_name='producto'
   success_url=reverse_lazy('accounts:homeTemplate')