from django.shortcuts import (
    render,redirect
)
from django.http import HttpResponse,HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView
from .models import Room
from .forms import RoomForm

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
# rooms=[
#     {'id':1,'name':"Lets Learn Python"},
#     {"id":2,"name":"JavaScript is the best"},
#     {"id":3,"name":"Then why is C++ still used for DSA"}
# ]
# def home(request):
#     context={'rooms':rooms}
#     return render(request,'myapp/home.html',context)
# remember in app sepecific templates templates-> app name-> html files
# if directly templates-> html that is treated global level thing
# def room(request,pk):
#     try:
#         # next returns first itwrator jhn match and break
#         room=next((i for i in rooms if i['id']==pk),None)
#         if room is None:
#             return HttpResponseNotFound("Room not found")
#         context={'room':room}
#         return render(request,'myapp/room.html',context)
#     except ValueError:
#         return HttpResponseNotFound("Invalid room ID")
def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'myapp/home.html',context)
def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'myapp/room.html',context)
def createRoom(request):
    if request.method=='POST':
        print(request.POST)
        form=RoomForm(request.POST) #Bind form with submitted data in that pae
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RoomForm()
    # form automatically generates that html
    print(form)
    context={'form':form}
    return render(request,'myapp/room_form.html',context)
def updateRoom(request,pk):
    room=Room.objects.get(id=1)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room) # Here putting the new room
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RoomForm(instance=room) # Here loaded exisint data
        # i.e. us room ki hi data we loaded so that its easy to change
    context={'form':form}
    return render(request,'myapp/room_form.html',context)
# Above I used same html template for both deletion as well as updationg
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'myapp/delete.html',{'obj':room})

