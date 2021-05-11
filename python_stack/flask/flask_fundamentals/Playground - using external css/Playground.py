from flask import Flask  , render_template
app = Flask(__name__)

@app.route("/")
def main():
    times = 0
    return render_template("index.html" , times = 3 , color = "aqua")

@app.route("/play/<x>")
def repeat(x=0):
    return render_template("index.html" , times = int(x) , color = "aqua")

@app.route("/play/<x>/<color1>")
def repeat_1(x= 0, times = 3 , color1="aqua"):
    return render_template("index.html" , times = int(x) , color = color1)


@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug = True)

