from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template('homepage.html')
    return HttpResponse (template.render())
def signinpage(request):
    template = loader.get_template('signinpage.html')
    return HttpResponse (template.render())
def signuppage(request):
    template = loader.get_template('signuppage.html')
    return HttpResponse (template.render())
def brands(request):
    template = loader.get_template('brands.html')
    return HttpResponse (template.render())
def rolex(request):
      template = loader.get_template('rolex.html')
      return HttpResponse (template.render())