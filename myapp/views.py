from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def base(request):
    name="bhavaikya"
    return render(request, "base.html",{'name':name })

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="bhavaikya"
    return render(request,"myapp/profile.html",{'name':name})

