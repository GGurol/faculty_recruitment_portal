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
            return redirect('page2')  

    return render(request, 'app/page1.html', {'page1_form': page1_form})

from .forms import PageForm2
from .models import PageModel2

def page2(request):
    user = request.user
    try:
        page2_data = PageModel2.objects.get(user=user)
        form = PageForm2(request.POST, instance=page2_data)
    except PageModel2.DoesNotExist:
        form = PageForm2(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            page2_data = form.save(commit=False)
            page2_data.user = user
            page2_data.save()
            return redirect('page3')
        
        return redirect('page3')

    return render(request, 'app/page2.html', {'page2_form': form})


from .models import PageModel3
from .forms import PageForm3
def page3(request):
    user = request.user
    try:
        page3_data = PageModel3.objects.get(user=user)
        form = PageForm3(request.POST, instance=page3_data)
    except PageModel3.DoesNotExist:
        form = PageForm3(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            page3_data = form.save(commit=False)
            page3_data.user = user
            page3_data.save()
            # Redirect to wherever you want to go after saving page 3 data
            return redirect('page4')
        # Redirect to 'some_page' after saving
        return redirect('page4')

    return render(request, 'app/page3.html', {'page3_form': form})

from .models import PageModel4
from .forms import PageForm4

def page4(request):
    user = request.user
    try:
        page3_data = PageModel4.objects.get(user=user)
        form = PageForm4(request.POST, instance=page3_data)
    except PageModel4.DoesNotExist:
        form = PageForm4(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            page4_data = form.save(commit=False)
            page4_data.user = user
            page4_data.save()
            return redirect('page5')
        return redirect('page5')
    return render(request, 'app/page4.html', {'page4_form': form})

from .models import PageModel5
from .forms import PageForm5


def page5(request):
    user = request.user
    try:
        page5_data = PageModel5.objects.get(user=user)
        form = PageForm5(request.POST or None, instance=page5_data)
    except PageModel5.DoesNotExist:
        form = PageForm5(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            page5_data = form.save(commit=False)
            page5_data.user = user
            page5_data.save()
            # Redirect to wherever you want to go after saving page 5 data
            return redirect('page6')
        # Redirect to 'some_page' after saving
        return redirect('page6')

    return render(request, 'app/page5.html', {'page5_form': form})


from .models import PageModel6
from .forms import PageForm6
def page6(request):
    user = request.user
    try:
        page6_data = PageModel6.objects.get(user=user)
        form = PageForm6(request.POST or None, instance=page6_data)
    except PageModel6.DoesNotExist:
        form = PageForm6(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            page6_data = form.save(commit=False)
            page6_data.user = user
            page6_data.save()
            # Redirect to wherever you want to go after saving page 6 data
            return redirect('page7')
        # Redirect to 'some_page' after saving
        return redirect('page7')

    return render(request, 'app/page6.html', {'page6_form': form})

from .models import PageModel7
from .forms import PageForm7

def page7(request):
    user = request.user
    try:
        page7_data = PageModel7.objects.get(user=user)
        form = PageForm7(request.POST or None, instance=page7_data)
    except PageModel7.DoesNotExist:
        form = PageForm7(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            page7_data = form.save(commit=False)
            page7_data.user = user
            page7_data.save()
            # Redirect to wherever you want to go after saving page 7 data
            return redirect('page8')
        # Redirect to 'some_page' after saving
        return redirect('page8')

    return render(request, 'app/page7.html', {'page7_form': form})

from .forms import PageForm8
from .models import PageModel8

def page8(request):
    if request.method == 'POST':
        form = PageForm8(request.POST, request.FILES)
        if form.is_valid():
            # Check if the user has already filled the form
            try:
                page_instance = PageModel8.objects.get(user=request.user)
                # If the user has already filled the form, update the existing instance
                form = PageForm8(request.POST, request.FILES, instance=page_instance)
            except PageModel8.DoesNotExist:
                pass  # No existing instance found, continue with creating a new one
            
            form.instance.user = request.user  # Assign the current user
            form.save()  # Save the form data
            
            return redirect('page9')  # Redirect to success page
    else:
        # Retrieve existing data from the database if available
        try:
            page_instance = PageModel8.objects.get(user=request.user)
            form = PageForm8(instance=page_instance)
        except PageModel8.DoesNotExist:
            form = PageForm8()  # No existing data, create a new form instance
        
    return render(request, 'app/page8.html', {'form': form})

from .models import PageModel9
from .forms import PageForm9

def page9(request):
    if request.method == 'POST':
        form = PageForm9(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to success page after form submission
    else:
        # If it's a GET request, retrieve existing data from the database (if any)
        try:
            instance = PageModel9.objects.filter().first()  # Get the first instance if multiple exist
            form = PageForm9(instance=instance)
        except PageModel9.DoesNotExist:
            form = PageForm9()

    return render(request, 'app/page9.html', {'form': form})


from django.conf import settings
import os
from pathlib import Path
from django.http import FileResponse
from django.views import generic
from .models import PDFFiles

# def success_page(request):
#     return render(request, 'app/success.html')

# def download(request):
#     context = {'pdffiles':PDFFiles.objects.all()}
#     return render(request, 'app/download.html',context)

# class download(generic.ListView):
#     model = PDFFiles
#     template_name = 'app/download.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["pdffiles"] = PDFFiles.objects.all()
#         return context
    

class SuccessView(generic.ListView):
    model = PDFFiles
    template_name = 'app/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pdf_url"] = PDFFiles.objects.first().file.url  # Assuming you only want to display the first PDF file
        return context