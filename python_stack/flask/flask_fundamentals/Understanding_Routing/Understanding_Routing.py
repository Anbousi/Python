from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_world_1():
    return "<h1>dojo</h1>"

@app.route('/say/<name>')
def hello_world_2(name):
    return "Hi " + name

#repeat word 
@app.route('/repeat/<int:num>/<word>') #contvert the number to integer instead of string "when we get the num from url it will be string so convert it to int"
def repeat(num , word):
    string = "" # define empty string to add repeated "word" with a Tag if needed
    for i in range(int(num)):
        string += "<p>" + word + "</p>" #define the Tag type if needed "first letter is capitalized"
    return string

#handle error 404
# @app.errorhandler(werkzeug.exceptions.BadRequest)
# def handle_bad_request(e):
#     return 'bad request!', 400

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.