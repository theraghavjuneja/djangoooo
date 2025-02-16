from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# def home(request):
#     return HttpResponse("Hey, You are Welcomed To The Home Page!!!")
# def about(request):
#     return HttpResponse("Hey, this is the about page? Ok")
# class HomeView(TemplateView):
#     # to render html pages without extra logic
#     # static pages about us faq etc.
#     template_name='home.html'
# class AboutView(View):
#     # used when more control needed(dynamic pages, API responses etc)
#     # to see a template return render(reqesu, 'home.html')

#     def get(self,request):
#         return HttpResponse("This page is using a CBV")
# rooms=[
#     {'id':1,'name':"Lets Learn Python"},
#     {"id":2,"name":"JavaScript is the best"},
#     {"id":3,"name":"Then why is C++ still used for DSA"}
# ]
# def home2(request):
#     context={'rooms':rooms}
#     # This will render home2.html of global templates (passed a context dict)
#     return render(request,'home2.html',context)
rooms=[
    {'id':1,'name':"Lets Learn Python"},
    {"id":2,"name":"JavaScript is the best"},
    {"id":3,"name":"Then why is C++ still used for DSA"}
]
def home(request):
    context={'rooms':rooms}
    return render(request,'myapp/home.html',context)
# remember in app sepecific templates templates-> app name-> html files
# if directly templates-> html that is treated global level thing
def room(request,pk):
    try:
        pk=int(pk)
        # next returns first itwrator jhn match and break
        room=next((i for i in rooms if i['id']==pk),None)
        if room is None:
            return HttpResponseNotFound("Room not found")
        context={'room':room}
        return render(request,'base/room.html',context)
    except ValueError:
        return HttpResponseNotFound("Invalid room ID")