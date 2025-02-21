from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    
    # If topic is deleted, room is not to be deleted
    # Topic class isse upr hai isiliye u can directly use,
    # agar niche hota to use 'Topic' , on_delete= jo bhi i.e. 'Topic' in ''
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    # related name allows u to reference this relationship from user model
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    # auto_now means whenever field change store
    updated=models.DateTimeField(auto_now=True)
    # now add means jab add hua bas tab store, not when edited
    created=models.DateTimeField(auto_now_add=True)
    # added later on (class Meta)
    class Meta:
        # dash means inverted newest updated sbe phle aayege
        
        ordering=['-updated','-created']
    def __str__(self):
        return self.name
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # room= models.ForeignKey(Room,on_delete=models.SET_NULL)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    # 
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        # dash means inverted newest updated sbe phle aayege
        
        ordering=['-updated','-created']
    def __str__(self):
        # display only first 50 char, (if a long message)
        return self.body[0:50]

    
