from django.shortcuts import render , redirect 
import random
from time import gmtime, strftime

# Create your views here.
def main(request):
    if "total" not in request.session:
        request.session.clear()
        request.session['total'] = 0
        request.session['log'] = []
        request.session['minus'] = 0


    context = {
        "total": request.session['total'],
        "minus": request.session['minus'],
        'win': request.session['log'],
    }
    return render(request,"index.html", context)

def gold(request):
    if request.method == 'POST':
        if request.POST['money'] == 'farm_gold':
            request.session['x'] = random.randint(10 , 20)
            request.session['total'] += request.session['x']
            request.session['minus'] = 0
            request.session['win'] = f"Earned {request.session['x']} golds from the farm! " + str(strftime("%H:%M %p", gmtime()))
            return redirect('/win')

            


        elif request.POST['money'] == 'cave_gold':
            request.session['y'] = random.randint(5 , 10)
            request.session['total'] += request.session['y']
            request.session['minus'] = 0
            request.session['win'] = f"Earned {request.session['y']} golds from the cave! " + str(strftime("%H:%M %p", gmtime()))
            return redirect('/win')
            

        elif request.POST['money'] == 'house_gold':
            request.session['z'] = random.randint(2 , 5)
            request.session['total'] += request.session['z']
            request.session['minus'] = 0
            request.session['win'] = f"Earned {request.session['z']} golds from the house! " + str(strftime("%H:%M %p", gmtime()))
            return redirect('/win')

        elif request.POST['money'] == 'casino_gold':
            if request.session['total'] > 0:
                request.session['c'] = random.randint(-50 , 50)
            else:
                request.session['minus'] = 1
                return redirect('/')
            request.session['total'] += request.session['c']
            if request.session['c'] >= 0:
                request.session['win'] = f"Earned {request.session['c']} golds from the casino! " + str(strftime("%H:%M %p", gmtime()))
            elif request.session['c'] < 0:
                request.session['win'] = f"Entered a casino and lost {request.session['c']} golds Ouch.. " + str(strftime("%H:%M %p", gmtime()))
            return redirect('/win')

    return redirect('/')

def win(request):
    log = request.session['log']
    log.append(request.session['win']) 
    request.session['log'] = log
    print(log)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')