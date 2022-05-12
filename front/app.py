from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return "hello"

@app.route('/ido/1')
def ido():  # put application's code here
    return render_template('home.html',skasks)


if __name__ == '__main__':
    app.run()
