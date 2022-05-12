from flask import Flask, render_template, request, flash
from back.queries import open_ticket

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'GET':
        return render_template('template.html')

    print(request.values)
    print(request.form)
    form = request.form
    # assert_input(request)
    # open_ticket(form["ticket_title"],
    #             form["ticket"],
    #             # form["urgency"]
    #             1234,
    #
    #             )

    return render_template('template.html')


@app.route('/<building>/<classroom>', methods=['GET', 'POST'])
def classroom_page(building, classroom):
    print(request.method)
    if request.method == 'GET' or assert_input(request.form,
                                               ["ticket_title", "ticket"]):
        return render_template('template.html')

    print(request.values)
    print(request.form)
    open_ticket(title=request.form["ticket_title"],
                desc=request.form["ticket"],
                urgency=int(request.form["urgency"]),
                building_name=building,
                room=classroom,
                )
    return render_template('template.html')


def assert_input(req, input_list):
    missing = False
    for item in input_list:
        if req.get(item) == '':
            flash(f"{item} is missing", category="error")
            pass
        return missing
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0")
