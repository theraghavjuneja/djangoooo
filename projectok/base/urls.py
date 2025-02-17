from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name="login"),
    path('',views.home,name="home"),
    # path('room/',views.room,name="room")
    # for dynamic rendering or dynamic room/1 room/2
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room")
]