from django.shortcuts import render,redirect
from django.db.models import Q #with q we can wrap search parameyers or/and
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Room,Topic,Message
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User doesnt exist')
        user=authenticate(request,username=username,password=password)
        if user is not None: # i.e. user is good
            login(request,user) #login adds session in database etc
            return redirect ('home')
        else:
            messages.error(request,'Username or password doesnt exist')


    context={'page':page}
    return render(request,'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('home') 
def registerUser(request):
    # page='register'
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) 
            user.username=user.username.lower()
            user.save()
            login(request,user) #login the necessary user
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
    return render(request,'base/login_register.html',{'form':form})
def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else '' # to get the query i.e. ?q="what"
    # rooms=Room.objects.all()
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q))
    room_count=rooms.count() #BETTER THAN PYTOON LEN
    topics=Topic.objects.all()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    print(context)
    return render(request,'base/home.html',context)
def room(request,pk):
    room=Room.objects.get(id=pk) # get the room having id=pk
    # retrieve all messages related to a specific room object
    room_messages=room.message_set.all().order_by('-created')
    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        # redirect reloads the page
        return redirect('room',pk=room.id)
    print(room_messages)
    context = {'room': room, 'room_messages': room_messages}
    return render(request,'base/room.html',context)
@login_required(login_url='login')
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
@login_required(login_url='login')
def updateRoom(request,pk):
    '''
    pk: To specify what room are we updating 
    - we need to prefill the data, unlike createRoom
    For that we use instance=room
    '''
    room=Room.objects.get(id=pk) #get the room id=pk
    form=RoomForm(instance=room)
    if request.user!=room.host:
        
        return HttpResponse('You are not allowed here')
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room) #need to specify instance so that django can validate
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.user!=room.host:
        return HttpResponse('You are not allowed here')
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})