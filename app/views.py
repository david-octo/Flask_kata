from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/accueil/<value>/')
def accueil(value):
    return value

@app.route('/api/', methods=['GET', 'PUT'])
def api_get():
    if request.method == 'GET':
        return "my get"
    elif request.method == 'PUT':
        return "my put"

@app.route('/api/', methods=['POST'])
def api_post():
    return "my post"

@app.route('/api_json/', methods=['GET'])
def api_json():
    return {'nom': 'dupont', 'prenom': 'xavier'}



if __name__ == "__main__":
    app.run()