from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm
# from django.contrib.auth.decorators import login_required 


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            
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


from .forms import PageForm1
from .models import PageModel1

def page1(request):
    user = request.user
    try:
        application_data = PageModel1.objects.get(user=user)
        page1_form = PageForm1(request.POST or None, request.FILES or None, instance=application_data)
    except PageModel1.DoesNotExist:
        page1_form = PageForm1(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if page1_form.is_valid():
            page1_form.instance.user = user
            page1_form.save()
            return redirect('page2')  # Use return to properly redirect after saving data

    return render(request, 'app/page1.html', {'page1_form': page1_form})

def page2(request):
    context={}
    return render(request,'app/page2.html',context)

def page3(request):
    context={}
    return render(request,'app/page3.html',context)

def page4(request):
    context={}
    return render(request,'app/page4.html',context)

def page5(request):
    context={}
    return render(request,'app/page5.html',context)

def page6(request):
    context={}
    return render(request,'app/page6.html',context)

def page7(request):
    context={}
    return render(request,'app/page7.html',context)

def page8(request):
    context={}
    return render(request,'app/page8.html',context)


