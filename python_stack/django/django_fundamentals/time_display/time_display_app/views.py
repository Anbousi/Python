from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render
from time import gmtime, strftime


def time_display(request):
    context = {
        "year": strftime("%Y", gmtime()),
        "month": strftime("%B", gmtime()),
        "day": strftime("%A", gmtime()),
        "day_date": strftime("%d", gmtime()),
        "clock": strftime("%H:%M %p", gmtime())
        
    }
    return render(request,'index.html', context)

def time(request):
    return redirect('/')

# Create your views here.

