from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Saylani Welfer International Trust</h1>
    <p>Paragraph1</p>    
    <p>Paragraph2</p>    
    <p>Paragraph3</p>    
    <p>Paragraph4</p>    
    """




    
app.run(debug=True)    