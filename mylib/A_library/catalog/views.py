from turtle import title
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect, HttpResponse
from django.contrib.auth import login
from django import forms
from catalog import views
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import Signupform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from .forms import Signupform, Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from.import views
from catalog import views
from django.forms import models
from django.views.generic import ListView
from.models import Book
from.models import Student
from django.utils import timezone
from django.db.models import Q 
import json
from datetime import date
from.import forms, models


# Create your views here.
def index(request):
   return render(request, "index.html") 

 



def signup(request):
    firstname=''
    lastname=''
    emailvalue=''
    uservalue=''
    passwordvalue1=''
    passwordvalue2=''

    form= Signupform(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password1")
        passwordvalue2= form.cleaned_data.get("password2")
        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'signup.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(uservalue, password= passwordvalue1,
                                           email=emailvalue)
                user.save()


                login(request,user)

                fs.user= request.user

                fs.save()
                context= {'form': form}
                return render(request, 'signup.html', context)
            
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'signup.html', context)

           



##def pagelogin(request):
  
    uservalue=''
    passwordvalue=''

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'login.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'login.html', context )

    else:
        context= {'form': form}
        return render(request, 'login.html', context) 


def pagelogout(request):
    if request.method =="POST":
        logout(request)
        return redirect('index')





# admin only
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/add_book")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def Logout(request):
    logout(request)
    return redirect ("/")

# admin addbook

@login_required(login_url = '/admin_login')
def add_book(request):
    if request.method == "POST":
       book = request.POST['book_id']
       title = request.POST['title']
       isbn = request.POST['isbn']
       description = request.POST['description']
       date_of_publication = request.POST['date_of_publication']
       uploaded_by = request.POST['uploaded_by']
       book_status= request.POST['book_status']
       subject = request.POST['subject']


       books = Book.objects.create(book_id=book, title=title, isbn=isbn,description= description,date_of_publication=date_of_publication,uploaded_by=uploaded_by,book_status=book_status,subject=subject,)
       books.save()
       alert = True
       return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")


# view book
@login_required(login_url = '/admin_login')
def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})

 
 ##student profile
@login_required(login_url = '/student_login')
def profile(request):
    return render(request, "profile.html")
 # ##student   
@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html",{'students':students})
## student login and sign
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")
 ## signup student   
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        student_id = request.POST.get['id']
        student_name = request.POST['name']
        college = request.POST['college']
        registration_no = request.POST['regisration_no']

        gender = request.POST['gender']

        
      
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "signup.html", {'passnotmatch':passnotmatch})
        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(id=student_id,phone=phone, student_name=student_name, college=college, registration_no=registration_no,gender=gender, emaile=email)
        user.save()
        student.save()
        alert = True
        return render(request, "signup.html", {'alert':alert})
    return render(request, "signup.html")


#students infor
@login_required(login_url = '/student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id)
    Borrower = Borrower.objects.filter(student_id=student[0].user_id)
    li1 = []
    li2 = []

    for i in Borrower:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            t=(request.user.id, request.user.get_full_name, book.name,book.author)
            li1.append(t)

        days=(date.today()-i.date_borrowed)
        d=days.days
        fine=0  # for default time zero true and false 0
        if d>3:
            day=d-7
            fine=day*5000
        else:
            d>10
            fine=day*15000
            
                


        t=(Borrower[0].date_borrowed, Borrower[0].expected_date_return, fine)
        li2.append(t)
    return render(request,'student_issued_books.html',{'li1':li1, 'li2':li2})
