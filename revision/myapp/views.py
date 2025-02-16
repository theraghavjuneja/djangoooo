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
    # to render html pages without extra logic
    # static pages about us faq etc.
    template_name='home.html'
class AboutView(View):
    # used when more control needed(dynamic pages, API responses etc)
    # to see a template return render(reqesu, 'home.html')

    def get(self,request):
        return HttpResponse("This page is using a CBV")
