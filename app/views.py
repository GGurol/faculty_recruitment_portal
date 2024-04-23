from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.models import auth, User
from django.contrib import messages
# Create your views here.

def register(request):
    context={}
    return render(request,'app/page7.html',context)





# def form1(req):
#     context={}
#     return render(req,'app/page1.html',context)
# def register(req):
#     if req.method == 'POST':
#         first_name = req.POST['first_name']
#         last_name = req.POST['last_name']
#         email = req.POST['email']
#         username=first_name+last_name
#         password = req.POST['password']
#         password2 = req.POST['password2']
#         if(password == password2):
#             if User.objects.filter(email=email).exists():
#                 messages.info(req,'Email already exist')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email, password=password)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(req,'Password not equal')
#             return redirect('register')
#     else:
#         return render(req,'app/register.html')

# def login(req):
#     if req.method == 'POST':
#         # email = req.POST['email']
#         username=req.POST['email']
#         password = req.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(req,user)
#             return redirect('/')
#         else:
#             messages.info(req,'Invalid Username or password')
#             return redirect('login')
#     else:
#         return render(req,'app/login.html')

# def logout(req):
#     auth.logout(req)
#     return redirect('login')

# def forgotPassword(request):
#     context={}
#     return render(request,'app/forget_password.html',context)
