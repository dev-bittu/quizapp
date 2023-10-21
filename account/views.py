from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "account/login.html")

class Logout(View):
    def get(self, request):
        return render(request, "account/login.html")

class Register(View):
    def get(self, request):
        return HttpResponse(request, "This feature id diabled")
