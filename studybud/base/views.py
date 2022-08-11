from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Book
from .forms import BookForm

# Create your views here.

#rooms = [
 #   {'id':1, 'name':'CJ TRUNTER'},
 #   {'id':2, 'name':'ENGLISH COMPOSITION'},
 #   {'id':3, 'name':'UNDERSTANDING PURE MATHEMATICS'},
 #   ]


def home(request):
    rooms = Book.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context )

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password does not exist')   
    context = {}
    return render(request,'base/loginpage.html', context)

def room(request, pk):
    room = Book.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def adminlog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home2')
        else:
            messages.error(request,'username or password does not exist')   
    context = {}
    return render(request,'base/adminlog.html')

def addbook(request):
    form = BookForm()
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'base/addbook_form.html', context)

def deleteBook(request, pk):
    room = Book.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/deletebook.html', {'obj':room})

def home2(request):
    rooms = Book.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home2.html', context )

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(name__contains=searched)
        return render(request, 'base/search.html', {'searched': searched,'books' : books})
    else:
        return render(request, 'base/search.html', {})