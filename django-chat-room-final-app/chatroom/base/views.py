from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    print(context)
    return render(request,'base/home.html',context)
def room(request,pk):
    room=Room.objects.get(id=pk) # get the room having id=pk
    context={'room':room}
    return render(request,'base/room.html',context)
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        print(form)
        form=RoomForm(request.POST)
        print(form)
        if form.is_valid():
            # form.save() will automatically save the room
            # provided that RoomForm is a valid model having a class meta
            form.save()
            return redirect ('home') # Redirect used since I want to send the user to other page
    context={'form':form}
    return render(request,'base/room_form.html',context) # I want to render this page
def updateRoom(request,pk):
    '''
    pk: To specify what room are we updating 
    - we need to prefill the data, unlike createRoom
    For that we use instance=room
    '''
    room=Room.objects.get(id=pk) #get the room id=pk
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room) #need to specify instance so that django can validate
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})