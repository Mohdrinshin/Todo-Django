"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",UserRegistorView.as_view(), name = "home"),
    path("register/",UserRegistorView.as_view(), name = "register"),
    path("login/",LoginView.as_view(),name = "login"),
    path("logout/",LogoutView.as_view(),name ='logout'),
    path("add/",AddView.as_view(), name="add"),
    path("read/",ReadView.as_view(),name="readTask"),
    path("update/<int:pk>",Update.as_view(), name="update"),
    path("delete/<int:pk>",Delete.as_view(), name="delete"),
    path('specific/<int:pk>',TaskSpecific.as_view()),
    path("completed/<int:pk>",Completed_status.as_view(), name="completed"),
    path("forget/",ForgetView.as_view(), name ="forget"),
    path('otp/',Otp.as_view(),name = 'otp'),
    path("reset/",ResetView.as_view(),name = 'reset'),
    path('filter/',TaskFilter.as_view(), name = 'filter'),
    path('home',home),
    path('',IndexView.as_view(), name = 'index'),
]
