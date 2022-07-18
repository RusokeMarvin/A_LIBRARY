"""A_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproj ect.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.urls import path,include
from django.contrib import admin
from catalog.views import views

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('/', include('catalog.urls')),
    path('logout/',views.logout),
    path("add_book/", views.add_book, name="add_book"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("view_students/",views.view_students, name="view_students"),
    path('', include('catalog.urls')),
    path("view_books/", views.view_books, name="view_books"), 
    path("student_login/", views.student_login, name="student_login"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),

    path("profile/", views.profile, name="profile"),
    

   
    
     
]

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)