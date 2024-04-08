from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

def register(request):
    context={}
    return render(request,'app/register.html',context)

def login(request):
    pass
def forgotPassword(request):
    pass
