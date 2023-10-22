from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already login. Logout first")
            return redirect("index")
        return render(request, "account/login.html")

    def post(self, request):
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=uname, password=passwd)
        print(uname, passwd, user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("index")
        else:
            messages.warning(request, "Username or password is incorrect")
        return render(request, "account/login.html")

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logged out")
        return render(request, "account/login.html")

class Register(View):
    def get(self, request):
        return render(request, "account/register.html")
