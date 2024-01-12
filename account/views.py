from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            messages.info(request, "You are already login. Logout first")
            return redirect("index")

    else:
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("index")
        else:
            messages.warning(request, "Username or password is incorrect")
    return render(request, "account/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in")
            return redirect("index")

    else:
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = User.objects.filter(username=uname).first()
        if user is None:
            user = User(username=uname)
            user.set_password(passwd)
            user.save()
            login(request, user)
            messages.success(request, "User created")
            return redirect("index")
        else:
            messages.info(request, "User already exists.")
    return render(request, "account/register.html")
