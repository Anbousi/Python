from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

def home(request):
    return render(request , 'home.html')
    
def log_reg(request):

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
            if (login_user(request.POST)):
                return redirect('/home/')
    
    return redirect('/')



