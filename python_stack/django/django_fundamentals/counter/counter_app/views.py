from django.shortcuts import render, redirect , HttpResponse 

# Create your views here.
def index(request):
    
    if "count" not in request.session:
        request.session['count'] = 1 
        request.session['increment'] = 1
    else:
        request.session['count'] += 1

    if "real_count" not in request.session:
        request.session['real_count'] = 1
        request.session['increment'] = 1
    else:
        request.session['real_count'] += 1

    context={"count": request.session['count'],
            "real_count": request.session['real_count'],
            "count1": request.session['increment']}
    return render(request , "index.html" , context )

def counter(request):
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    request.session.pop("count")
    return redirect('/')

def hard_reset(request):
    request.session.clear()
    return redirect('/')

def inc(request):
    if request.POST['counti'] == '':
        return redirect('/')

    incr = int(request.POST['counti'])
    request.session['count'] += (incr-1)
    request.session['increment'] = request.POST['counti']
    return redirect('/')
