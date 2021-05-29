from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

def home(request):

    if 'login' in request.session: #if user already logged in before
        return render(request , 'home.html')
    return redirect('/')
    
def log_reg(request):

    if 'login' in request.session: #if user already logged in before
        return redirect('/home')

    return render(request,'log_reg.html')

def check(request):
    if request.method == 'POST':
        in_data = request.POST
        if in_data['log_reg'] == 'registration':
            errors = create_user(in_data)

            if len(errors)>0:
                for key,value in errors.items():
                    messages.error(request,value)
                return redirect('/')
            return redirect('/home')
            
        elif in_data['log_reg'] == 'login':
            if request.method == 'POST':
                errors = login_user(request.POST)
                if len(errors)>0:
                    for key,value in errors.items():
                        messages.error(request,value)
                    return redirect('/')

            if 'login' not in request.session: #if user already logged in before
                request.session['login'] = request.POST['email']
                return redirect('/home/')
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')



