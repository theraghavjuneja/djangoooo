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
    path('room/<str:pk>/',views.room,name='room')
]