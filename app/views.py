from flask import Flask
# from .src.compute_accuracy import compute_accuracy
from .models import db, Content

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

# @app.route('/compute/accuracy/')
# def compute():
#     accuracy = compute_accuracy()
#     db.session.add(Content(accuracy))
#     db.session.commit()
#     return "Inference done and added to database"
#
# @app.route('/database/')
# def query():
#     return Content.query.all()

if __name__ == "__main__":
    app.run()