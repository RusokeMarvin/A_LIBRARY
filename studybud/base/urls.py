from django.urls import path  
from . import views


urlpatterns = [
    
   
    path('', views.home, name="home"),  
    path('room/<str:pk>/', views.room, name="room"),
    path('login/',views.loginpage,name = "login"),
    path('sign/',views.signup,name = "signup"),
    
    

   
    
]
