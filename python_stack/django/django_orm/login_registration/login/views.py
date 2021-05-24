from django.shortcuts import render , redirect
from . import views , models

# Create your views here.
def main(request):

    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        if request.POST['login_type'] == "login":
            if models.check_user(request.POST['name'] , request.POST['password']):
                request.session['username'] = request.POST["name"]
                return render(request,'welcome.html')
            else:
                return redirect('/')

        elif request.POST['login_type'] == "registration":
            models.register(request.POST['name'] , request.POST['password'])

    return redirect('/')