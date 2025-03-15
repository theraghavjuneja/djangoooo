from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
rooms=[
    {'id':1,'name':'Lets learn Python!'},
    {'id':2,'name':'Design with me!'},
    {'id':3,'name':'Frontend developer'}
]
def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html',context)
def room(request,pk):
    for i in rooms:
        if i['id']==pk:
            room=i
            break
    context={'room':room}
    return render(request,'base/room.html',context)