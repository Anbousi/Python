from flask import Flask, render_template , request , redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keek it safe' #give the app a secret key
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users' , methods=['POST'])
def creat_user():
    print("Got Post Infon")
    print(request.form)
    session['username'] = request.form['name'] #instead of name = request.form['name]
    session['usermail'] = request.form['email'] # the data saved inside a session
    return redirect("/show") 
    # return render_template('show.html', name_on_template=name_from_form, email_on_template=email_from_form)

@app.route('/show')
def show_user():
    print("Showing the User Info From thr Form")
    # print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['usermail'])

if __name__ == "__main__":
    app.run(debug=True)
