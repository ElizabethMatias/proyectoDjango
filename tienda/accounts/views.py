from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class homeTemplate(TemplateView):
   template_name = "accounts/home.html"

class login(TemplateView):
   template_name = "accounts/login.html"