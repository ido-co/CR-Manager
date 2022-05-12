from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def home():
    print(request.values)
    print(request.form)
    return render_template('template.html')

@app.route('/class/<classroom>')
def classroom_page(classroom):

    return render_template('real_python_2.html',classroom = classroom)


if __name__ == '__main__':
    app.run()
