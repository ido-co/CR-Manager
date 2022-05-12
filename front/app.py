from flask import Flask, render_template, request
from back.queries import open_ticket

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'GET':
        return render_template('template.html')

    print(request.values)
    print(request.form)
    form = request.form
    assert_input(request)
    open_ticket(form["ticket_title"],
                form["ticket"],
                # form["urgency"]
                1234,

                )

    return render_template('template.html')


@app.route('/<building>/<classroom>', methods=['GET', 'POST'])
def classroom_page(building, classroom):
    print(request.method)
    if request.method == 'GET':
        return render_template('template.html')

    print(request.values)
    print(request.form)
    form = request.form
    assert_input(request)
    open_ticket(title=form["ticket_title"],
                desc=form["ticket"],
                # form["urgency"]
                building_name=building,
                room=classroom,
                )
    return render_template('template.html')


def assert_input(req , input_list):
    missing =[]
    pass


if __name__ == '__main__':
    app.run()
