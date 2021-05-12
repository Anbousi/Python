from flask import Flask , render_template , request , redirect
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result' , methods=['POST'])
def result():
    name_form = request.form['name']
    location_form = request.form['location']
    language_form = request.form['language']
    comment_form = request.form['comment']
    radio_form = request.form['radio']
    check_form = request.form['check']
    print(check_form)
    return render_template('result.html' , name_form = name_form , location_form = location_form , language_form = language_form , comment_form = comment_form )

if __name__ == '__main__':
    app.run(debug = True)