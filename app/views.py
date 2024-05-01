from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm
from .models import UserRegistration


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']  # You might want to hash the password before saving
            
            user = User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name, password=password)
            
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('page1')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('user_login')


def page1(request):
    context={}
    return render(request,'app/page1.html',context)


