from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name = "signup"),
    path('login',views.loginpage,name = "login"),
    path('home',views.home,name = "home"),
    path('room/<str:pk>/', views.room,name = "room"),
    path('adminlog',views.adminlog,name="adminlog"),
    path('addbook',views.addbook,name="addbook"),

    
]