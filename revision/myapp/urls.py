from django.urls import path
# from directory where url is located import views
from . import views
from django.urls import path
from . import views

# urlpatterns = [  # Corrected variable name
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('home_cbv/', views.HomeView.as_view(), name='home_cbv'),
#     path('about_cbv/', views.AboutView.as_view(), name='about_cbv'),
#     path('home2/',views.home2,name='Home2')
# ]

urlpatterns=[
    path('',views.home,name='home'),
    path('room/<int:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<int:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<int:pk>/',views.deleteRoom,name="delete-room")
]