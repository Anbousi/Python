from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def index(request):

    return render(request,"index.html")

def get_user(request):
    if request.method == "GET":
        print("this is GET method")
    if request.method == "POST":
        print("this is POST method")
    return render(request,"index.html")

def post_user(request):
    if request.method == "GET":
        print("this is GET method")
    if request.method == "POST":
        print("this is POST method")
        print(request.POST)
    return render(request,"index.html")