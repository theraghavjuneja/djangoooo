from django.db import models #models has tools for creating db-> which maps to sql
from django.contrib.auth.models import User #django built in auth model(Represents user who can login)
# Create your models here.
# Create DB Table called Topic
class Topic(models.Model):
    # a str field for storing topic names maxLen=200
    name=models.CharField(max_length=200)
    def __str__(self):
        # Will return topic name when printing instance
        return self.name
# TOPIC WIll look something like 
# ID  NAME 
# 1  Python
# 2 DJANGO
class Room(models.Model):
    # one to many relationship
    
    # user is a table
    # For one to many (Example) one user-> multiple rooms
    # therefore use foreign key in many waala (child)
    # one user can host many rooms, but each room only has one host
    # foreign keys adds a user column(called host) in Room table
    # since host can be repeated one host-> multiple rooms, so one to many

    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # There can be multiple rooms on same topic, but each room only one topic
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)

    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# a room-> one host, one host-> many rooms
# id host_id topic_id name Description updated created
# one to many & many to one is kinda same, from one side we say one to many
# one category-> many products(Category class)
# many products-> one category(Product class)

# many to many
# similarly u can make one to one field etc too
# class Student(models.Model):
#     name=models.CharField(max_length=100)
# class Course(models.Model):
#     name=models.CharField(max_length=100)
#     students=models.ManyToManyField(Student)
#     c=models.one