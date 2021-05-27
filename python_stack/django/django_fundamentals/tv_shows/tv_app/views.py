from django.shortcuts import render , redirect 
from tv_app.models import *
from time import strftime
from django.contrib import messages

# Create your views here.
def read_all(request):
    context = {
        'shows': read_shows()
    }
    return render(request,'read_all.html', context)

def new(request):
    return render(request, 'add_show.html')

def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect ('/shows/new')

    if request.method == ['POST']:
        new_show = create_show(request.POST)
        return redirect ('/shows/'+str(new_show.id))

def show_this(request,id):
    context = {
        "this_show": this_show(id)
    }
    return render(request , 'show_this.html' , context)

def delete(request,id):
    delete_this(id)
    return redirect('/shows')

def edit(request,id):
    time = this_show(id).release_date
    context = {
        "this_show": this_show(id),
        "date": time.strftime('%Y-%m-%d')
    }
    return render(request, 'edit_this.html' , context)

def update(request,id):
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect (f'/shows/{id}/edit')

    editted_show = update_show(request.POST)
    return redirect('/shows/'+str(id))