from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
# Create your views here.
def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def creat(request):
    return redirect('/')

def show(request, number):
    return HttpResponse('placeholder to display blog number ' + str(number))

def edit(request , number):
    return HttpResponse('placeholder to edit blog ' + str(number))

def destroy(request, number):
    return redirect('/blogs')

def json(request):
    Bonus = {
        'title': "My first blog",
        "content": "Hi there, this is my first project using Django"
    }
    return JsonResponse({'Bonus': Bonus})