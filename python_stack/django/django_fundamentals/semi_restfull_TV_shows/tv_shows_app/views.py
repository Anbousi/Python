from django.shortcuts import render , redirect
from tv_shows_app.models import *
from time import strftime

# Create your views here.
def main(request):
    context = {
        'tv_shows': show_tv()
    }
    return render(request,'show_all.html' , context)

def new(request):
    return render(request,'new.html')

def create(request):
    new_show = create_show(request.POST)
    return redirect('/shows/'+str(new_show.id))

def show_this(request,id):
    context = {
        'show_this': Shows.objects.get(id=id)
    }
    return render(request,'show_this.html', context)

def delete(request,id):
    delete_this(id)
    return redirect('/shows')

def edit(request,id):
    this_show_date = edit_this(id).release_date
    context = {
        'edited_show': edit_this(id),
        "time": this_show_date.strftime('%Y-%m-%d')
    }
    return render(request , 'edit_this.html' , context)

def update(request,id):
    show = Shows.objects.get(id=id)    
    show.title = request.POST['title']

    show.save()
    return redirect(f'/shows/{id}')


