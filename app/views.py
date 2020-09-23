from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/accueil/<value>/')
def accueil(value):
    return value

@app.route('/api_get/', methods=['GET'])
def api_get():
    return "my get"




if __name__ == "__main__":
    app.run()