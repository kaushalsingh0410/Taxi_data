print('Ritu')
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',fare = '$0.0')

    # predict


if __name__ == '__main__':
    app.run(debug = True)