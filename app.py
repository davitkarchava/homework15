from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    subjects = ["საქართველო", "თურქეთი", "აზერბაიჯანი", "რუსეთი", "სომხეთი"]
    return render_template('index.html', subjects=subjects)


@app.route('/<name>/<int:age>')
def user(name, age):
    return render_template('user.html', name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)
