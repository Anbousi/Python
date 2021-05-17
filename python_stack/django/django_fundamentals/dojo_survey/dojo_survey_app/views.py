from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def index(request):

    return render(request,"index.html")

def data(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['radio'] = request.POST['radio']
        # check = request.POST['check']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')

def result(request):
    context = {
    "name": request.session['name'],
    "location" : request.session['location'],
    "language" : request.session['language'],
    "radio": request.session['radio'],
    # "check" : check,
    "comment": request.session['comment']
    }
    return render(request,"result.html" , context)


