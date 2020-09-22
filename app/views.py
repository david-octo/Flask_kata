from flask import Flask, render_template
from app.models import db, Content
from app.src.compute_accuracy import model_pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/compute/')
def compute():
    accuracy = model_pipeline()
    return render_template('accuracy.html', accuracy=accuracy)


if __name__ == "__main__":
    app.run()