from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return HttpResponse("Hey, You are Welcomed To The Home Page!!!")
def about(request):
    return HttpResponse("Hey, this is the about page? Ok")
class HomeView(TemplateView):
    template_name='home.html'
class AboutView(View):
    def get(self,request):
        return HttpResponse("This page is using a CBV")
