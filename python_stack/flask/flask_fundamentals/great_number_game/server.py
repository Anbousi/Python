from flask import Flask , render_template , redirect , request , session
import random

from werkzeug.wrappers.base_request import _assert_not_shallow
app = Flask(__name__)
app.secret_key= "secret key!"

@app.route('/')
def main():
    if 'random_num' not in session:
        session['random_num'] = random.randint(0,100)
    if 'answer' not in session:
        session['answer'] = ""

    if 'estimated' not in session:
        session['estimated'] =""

    if 'color' not in session:
        session['color'] = 'grey'
    
    if 'count' not in session:
        session['count'] = 0
    
    if 'win' not in session:
        session['win'] = 0
    
    return render_template('index.html' , x = session['random_num'] , answer = session['answer'] , estimated = session['estimated'], color = session['color'] , y = session['count'], win = session['win'])

@app.route('/guess-num', methods =['POST'])
def guess_num():
    session['guess_num'] = request.form['num_guess']
    session['count'] += 1
    return redirect('/calculations')

@app.route('/calculations')
def calculations():

    if int(session['random_num']) == int(session['guess_num']):
        session['answer'] = 'Right'
    else:
        session['answer'] = 'Wrong'

    if int(session['guess_num']) < (int(session['random_num'])) and (int(session['guess_num']) >= (int(session['random_num']))-5):
        session['estimated'] = 'Very Close Low'
        session['color'] = "lightgreen"
    elif int(session['guess_num']) < (int(session['random_num'])) and (int(session['guess_num']) >= (int(session['random_num']))-10):
        session['estimated'] = 'Low'
        session['color'] = 'lightpink'
    elif int(session['guess_num']) < (int(session['random_num'])):
        session['estimated'] = 'Too Low'
        session['color'] = 'red'
    elif int(session['guess_num']) > (int(session['random_num'])) and (int(session['guess_num']) <= (int(session['random_num']))+5):
        session['estimated'] = 'Very Close Heigh'
        session['color'] = "lightgreen"
    elif int(session['guess_num']) > (int(session['random_num'])) and (int(session['guess_num']) <= (int(session['random_num']))+10) :
        session['estimated'] = 'Heigh'
        session['color'] = 'lightpink'
    elif int(session['guess_num']) > (int(session['random_num'])):
        session['estimated'] = 'Too Heigh'
        session['color'] = 'red'
    elif int(session['random_num']) == int(session['guess_num']):
        session['estimated'] = 'Great'
        session['color'] = 'green'
        session['answer'] = str(session['random_num']) + '\nWas the number'
        return redirect('/win')
    return redirect('/')

@app.route('/reset', methods =['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/win')
def win():
    session['win'] = 1
    print("You Win")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
