from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# part 2 of db etc
from .models import (
    Room,
    Topic,
    Message)
from django.db.models import Q
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
# Create your views here.
from django.http import HttpResponse
from .forms import RoomForm
rooms=[
    {'id':1,'name':'Lets learn Python!'},
    {'id':2,'name':'Design with me!'},
    {'id':3,'name':'Frontend developer'}
]
def home(request):
    # return HttpResponse('Home page')
    # since templates added
    # return render(request,'home.html')

    # now this room is passed to templaye

    # called as context dict
    # context={'rooms':rooms}

    # changed from home.html to appspecific template
    # return render(request,'home.html',context)

    # return render(request,'base/home.html',context)

    # to get access to all rooms
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    # i contains just make sure even if we do pyt to wo search kre
    # there are various options start with ends with etc
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q))
    # rooms=Room.objects.all()
    topics=Topic.objects.all()
    room_count=rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/home.html',context)

# for both login and logout we are redirecting to same html only
# thus in both endpoints I created a page name so which I can pass as context so that html template which know which section to render

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    # for post
    if request.method=='POST':
        # i.e. user entered info
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist: #if the username is wrong
            messages.error(request,'User does not exist')
            return render(request, 'base/login_register.html')
        user=authenticate(request,username=username,password=password)
        if user is not None: 
            login(request,user)
            return redirect('home')
        else: # it is trigerred when credentials wron
            messages.error(request,'Username or password does not exist')
    # for get
    context={'page':page}
    return render(request,'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('home')
def registerUser(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            # to access the user 
            user=form.save(commit=False) #gives an unsaved user object
            # Now Lowering
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Sorry an error occured during registration')
    return render(request,'base/login_register.html',{'form':form})
# now also add pk
def room(request,pk):
    # return HttpResponse('ROOM')
    # return render(request,'room.html')
    # added at last this 
    # for i in room s:
    #     if i['id']==int(pk):
    #         room=i
    # # whatever id matches wo 
    # context={'room':room}
    # return render(request,'base/room.html',context)

    # to get a room (Example if /1 called to get room1 (id))
    # id auto generated
    room=Room.objects.get(id=pk) # Retrieve a room object id=pk
    # SUppose Message linked to Room using FK, then a reverse relation also created called message_set
    # By adding related name query we can customize it
    # used to retrieve that
    room_messages=room.message_set.all().order_by('-created')
    # To avoid flash messages being shown we replaces messages by room_messages
    participants=room.participants.all() #many to many-> can directly do .all() 









    if request.method=='POST':
        # i will be creating a message object with user room and message bid
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        # i can add this user in room
        room.participants.add(request.user)
        return redirect('room',pk=room.id)



    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)
@login_required(login_url='login')
def createRoom(request):
    # send user back to home page if he is valid
    form=RoomForm()
    if request.method=='POST':
        print(request.POST)
        form=RoomForm(request.POST)
        if form.is_valid():
            # save in db then
            form.save()
            # since name='home' I can directly do this
            return redirect('home')

    context={'form':form}
    return render(request,'base/room_form.html',context)
    # context={}
    # return render(request,'base/room_form.html',context)
@login_required(login_url='login')
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    # prefelling this form with that room value
    if request.user!=room.host:
        return HttpResponse('You cant update somebody else room')
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        # here we replace original data by this
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.user!=room.host:
        return HttpResponse('You cant delete somebody else room')
    if request.method=='POST':
        room.delete()
        return redirect('home')
    
    return render(request,'base/delete.html',{'obj':room})
@login_required(login_url='login')
def deleteMessage(request,pk):
    message=Message.objects.get(id=pk)
    if request.user!=message.user:
        return HttpResponse('You are not allowed here')
    if request.method=='POST':
        message.delete()
        return redirect('home')
    
    return render(request,'base/delete.html',{'obj':message})