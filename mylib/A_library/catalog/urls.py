from django.contrib import admin
from django.urls import path,include
from catalog import views
from .models import *
from django.contrib import admin
from .views import signup,student_login
from catalog.views import add_book,view_students,view_books,profile

urlpatterns = [
     path("", views.index, name="index"),
     path("admin_login/", views.admin_login, name="admin_login"), 
     path('signup/',views.signup, name='signup'), 
     path("add_book/", views.add_book, name="add_book"),
     path("view_students/",views.view_students, name="view_students"),
     path('view_students/',views.view_students, name='view_students'),
     path("view_books/", views.view_books, name="view_books"), 
     path("student_login/", views.student_login, name="student_login"),
     path("student_issued_books/", views.student_issued_books, name="student_issued_books"),

     path("profile/", views.profile, name="profile"),

 
]

urlpatterns = [
 path('',views.index, name="index"),
 
 
]