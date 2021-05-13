from flask import Flask , render_template , redirect , request , session
app = Flask(__name__)
app.secret_key = "Secret key"
count = 1
@app.route('/')
def index():
    if 'real_counter' and 'counter' in session:
        session['counter'] += count
        session['real_counter'] += 1

    else:
        session['counter'] = 1
        if 'real_counter' not in session:
            session['real_counter'] = 1
        session['increment'] = 1
        
    return render_template("index.html" , count = session['counter'] , count1 = session['increment'] , real_count = session['real_counter'])


@app.route('/counter' , methods=['POST'])
def counters():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset' , methods=['POST'])
def reset_count():
    # session.pop('counter') #clear specific key
    # session.clear() #clear all keys
    #session.clear()
    session.pop('counter')
    return redirect('/')

@app.route('/hard_reset' , methods=['POST'])
def hard_reset_count():
    session.clear()
    return redirect('/')

@app.route('/inc' , methods=['POST'])
def num_count():
    count = request.form['count']
    session['increment'] = count
    session['counter'] += int(count)-1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)