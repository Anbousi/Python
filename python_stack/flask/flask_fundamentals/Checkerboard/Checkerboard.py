from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def chess():
    return render_template('index.html', x=8 , y=8 , color1 = "orange" , color2 = "red")

@app.route('/<int:x1>')
def chess1(x1):
    return render_template('index.html', x=x1 , y=8 , color1 = "orange" , color2 = "red")

@app.route('/<int:x1>/<int:y1>')
def chess2(x1,y1):
    return render_template('index.html', x=x1 , y=y1 , color1 = "orange" , color2 = "red")

@app.route('/<int:x1>/<int:y1>/<color1>/<color2>')
def chess3(x1,y1,color1,color2):
    return render_template('index.html', x=x1 , y=y1 , color1 = color1 , color2 = color2)

if __name__ == "__main__":
    app.run(debug = True)