from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse , redirect
import random

# Create your views here.
def main(request):
    
    if 'random_num' not in request.session:
        request.session['random_num'] = random.randint(0,100)
        print(request.session['random_num'])
        request.session['value1'] = 0
        print(request.session['value1'])
    if 'answer' not in request.session:
        request.session['answer'] = ""

    if 'estimated' not in request.session:
        request.session['estimated'] =""

    if 'color' not in request.session:
        request.session['color'] = 'grey'
    
    if 'count' not in request.session:
        request.session['count'] = 0
    
    if 'win' not in request.session:
        request.session['win'] = 0
        
    context = {
        "x": request.session['random_num'] ,
        "answer" : request.session['answer'] ,
        "estimated" : request.session['estimated'],
        "color" : request.session['color'] ,
        "y" : request.session['count'],
        "win" : request.session['win'],
        "value1" : request.session['value1'],
    }
    
    return render(request, 'index.html' , context )

def guess_num(request):
    if request.method == "POST":
        request.session['guess_num'] = request.POST['num_guess']
        request.session['count'] += 1
        request.session['value1'] = request.session['guess_num']
        # print(request.session['guess_num'] , request.session['count'])
        print(request.session['value1'] , ".............")
        return redirect('/calculations')

def calculations(request):
    if int(request.session['random_num']) == int(request.session['guess_num']):
        request.session['answer'] = 'Right'
    else:
        request.session['answer'] = 'Wrong'

    if int(request.session['guess_num']) < (int(request.session['random_num'])) and (int(request.session['guess_num']) >= (int(request.session['random_num']))-5):
        request.session['estimated'] = 'Very Close Low'
        request.session['color'] = "lightgreen"
    elif int(request.session['guess_num']) < (int(request.session['random_num'])) and (int(request.session['guess_num']) >= (int(request.session['random_num']))-10):
        request.session['estimated'] = 'Low'
        request.session['color'] = 'lightpink'
    elif int(request.session['guess_num']) < (int(request.session['random_num'])):
        request.session['estimated'] = 'Too Low'
        request.session['color'] = 'red'
    elif int(request.session['guess_num']) > (int(request.session['random_num'])) and (int(request.session['guess_num']) <= (int(request.session['random_num']))+5):
        request.session['estimated'] = 'Very Close Heigh'
        request.session['color'] = "lightgreen"
    elif int(request.session['guess_num']) > (int(request.session['random_num'])) and (int(request.session['guess_num']) <= (int(request.session['random_num']))+10) :
        request.session['estimated'] = 'Heigh'
        request.session['color'] = 'lightpink'
    elif int(request.session['guess_num']) > (int(request.session['random_num'])):
        request.session['estimated'] = 'Too Heigh'
        request.session['color'] = 'red'
    elif int(request.session['random_num']) == int(request.session['guess_num']):
        request.session['estimated'] = 'Great'
        request.session['color'] = 'green'
        request.session['answer'] = str(request.session['random_num']) + '\nWas the number'
        return redirect('/win')
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

def win(request):
    request.session['win'] = 1
    print("You Win")
    return redirect('/')