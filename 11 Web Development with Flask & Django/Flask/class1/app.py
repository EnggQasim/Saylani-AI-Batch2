from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/about")
def about():
    return "<h1>About!</h1>"


    
app.run(debug=True, port=1000)    