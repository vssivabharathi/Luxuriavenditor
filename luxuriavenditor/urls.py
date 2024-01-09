"""
URL configuration for luxuriavenditor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from lvapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from lvapp import templates
urlpatterns = [
  path("",views.index, name="home"),
  path("index",views.index, name="homepage"),
    path("signinpage",views.signinpage, name="signinpage"),
    path("signuppage",views.signuppage, name="signuppage"),
    path("brands",views.brands, name="brands"),
    path("rolex",views.rolex, name="rolex")
    
]
urlpatterns += staticfiles_urlpatterns()