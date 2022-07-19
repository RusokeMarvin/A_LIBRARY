from django.shortcuts import redirect, render
from .models  import Room
from django.contrib.auth import authenticate, login, logout

 

# Create your views here.

# rooms =[
#    {'id':1, 'name':'Lets learn python!'},
#   {'id':2, 'name':'Design with me'},
#  {'id':3, 'name':'Frontend developpers'},
#]


def home(request):
    rooms= Room.objects.all()
    context = {'rooms': rooms} 
    return render(request, 'base/home.html', context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}        
    
    return render(request, 'base/room.html', context)


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

def signup(request):
    return render(request,'base/signup.html')




