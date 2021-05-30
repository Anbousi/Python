from django.shortcuts import redirect, render
from django.contrib import messages
from the_wall_app.models import *

def home(request):

    if 'login' in request.session: #if user already logged in before
        this_user = get_this_user(request.session['email'])
        print(this_user)
        print("**************************")
        print(get_all_messages())
        print(this_user)
        print(get_messages(this_user.email))
        context = {
            'messages' : get_messages(this_user.email),
            'user': this_user
        }
        return render(request , 'home.html' , context)
    return redirect('/')
    
def log_reg(request):

    if 'login' in request.session: #if user already logged in before
        return redirect('/home')

    return render(request,'root.html')

def check(request):
    if request.method == 'POST':
        in_data = request.POST
        if in_data['log_reg'] == 'registration':
            errors = create_user(in_data)

            if len(errors)>0:
                for key,value in errors.items():
                    messages.error(request,value)
                return redirect('/')
            if 'login' not in request.session: #if user already logged in before
                request.session['login'] = request.POST['f_name']
                request.sessiom['name'] = request.POST['f_name']
            return redirect('/home')
            
        elif in_data['log_reg'] == 'login':
            if request.method == 'POST':
                errors = login_user(request.POST)
                if len(errors)>0:
                    for key,value in errors.items():
                        messages.error(request,value)
                    return redirect('/')
            user = get_user(request.POST['email'])
            if 'login' not in request.session: #if user already logged in before
                request.session['login'] = user[0].first_name
                request.session['email'] = user[0].email
                return redirect('/home/')
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def post_message(request):
    print(request.session['email'])
    user = get_this_user(request.session['email'])
    print(user.first_name)
    p_message(user.id,request.POST['p_message']) #create a post message
    return redirect('/home/')