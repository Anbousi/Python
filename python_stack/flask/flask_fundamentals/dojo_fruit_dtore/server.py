from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawbarry = request.form['strawberry']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    blackberry = request.form['blackberry']
    f_name = request.form['first_name']
    l_name = request.form['last_name']
    std_id = request.form['student_id']
    count = int(strawbarry) + int(apple) + int(raspberry) + int(blackberry)
    print(request.form)
    print(f"Charging {f_name} {l_name} for {count} fruits")

    return render_template("checkout.html",strawbarry = strawbarry , apple = apple , raspberry = raspberry ,blackberry = blackberry , f_name = f_name , l_name = l_name, std_id = std_id , count = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    