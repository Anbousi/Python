from flask import Flask , render_template , redirect , request , session
app = Flask(__name__)
app.secret_key = "Secret key"

@app.route('/')
def index():
    session['add'] = 0
    session['reset'] = 0
    print(session['add'] , session['reset'] )
    if 'counter' in session:
        session['counter'] += 1
        print(session['counter'])
    else:
        session['counter'] = 1
        
    return render_template("index.html" , count = session['counter'])


@app.route('/counter' , methods=['POST'])
def counters():
    # session['add'] = request.form['add']
    # session['reset'] = request.form['reset']
    # if session['add']:
    #     print("added")
    #     session['counter'] += 1

    # if session['reset']:
    #     # session.pop('counter') #clear specific key
    #     session.clear() #clear all keys
    #     print(session['reset'])

    print("added")
    session['counter'] += 1

    return redirect('/')

@app.route('/reset' , methods=['POST'])
def reset_count():
    print("reseted")
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)