from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('page1/', views.page1, name='page1'),
    # path("", views.form1, name="form1"),
    # path('register/',views.register, name='register'),
    # path('login/',views.login, name='login'),
    # path('logout/',views.logout, name='logout'),
    # path('forgot-password/',views.forgotPassword,name="forgot-password"),
]
