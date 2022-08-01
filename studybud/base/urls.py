from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', user_views.signup, name='signup'),
    path('login/',views.loginpage,name = "login"),
    path('home/',views.home,name = "home"),
    path('room/<str:pk>/', views.room,name = "room"),
    path('delete-room/<str:pk>/', views.deleteBook,name = "delete-room"),
    path('adminlog/',views.adminlog,name="adminlog"),
    path('addbook/',views.addbook,name="addbook"),
    path('home2/',views.home2,name = "home2"),

    
]