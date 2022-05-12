from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/class/<classroom>')
def classroom_page(classroom):

    return render_template('real_python_2.html',classroom = classroom)


if __name__ == '__main__':

    app.run()
