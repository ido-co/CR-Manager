from flask import Flask, render_template, request, flash
from back.queries import open_ticket, inc_ac_counter, dec_ac_counter, get_classes

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'GET':
        pass
    return render_template('classroom_landing.html')

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
def classroom_landing_page(building, classroom):
    now, later = get_classes(building, classroom)
    return render_template('landing_page.html',
                           building=building,
                           room=classroom,
                           this_lesson=now,
                           next_lesson=later
                           )


AC_STATUS = False


@app.route('/<building>/<classroom>/ac', methods=['GET', 'POST'])
def classroom_ac_page(building, classroom):
    global AC_STATUS
    method = {"ON": inc_ac_counter,
              "OFF": dec_ac_counter}
    if request.method == "POST":
        AC_STATUS = method[request.form["ac"]](classroom, request.remote_addr)
    return render_template('ac.html',
                           building=building,
                           room=classroom,
                           ac_status=("on" if AC_STATUS else "off")
                           )


@app.route('/<building>/<classroom>/ticket', methods=['GET', 'POST'])
def classroom_ticket_page(building, classroom):
    if request.method == 'GET' or assert_input(request.form,
                                               ["ticket_title", "ticket"]):
        return render_template('ticket.html')

    open_ticket(title=request.form["ticket_title"],
                desc=request.form["ticket"],
                urgency=int(request.form["urgency"]),
                building_name=building,
                room=classroom,
                )
    return render_template('ticket.html')


def assert_input(req, input_list):
    missing = False
    for item in input_list:
        if req.get(item) == '':
            flash(f"{item} is missing", category="error")
            missing = True
    return missing


if __name__ == '__main__':
    app.run(host="0.0.0.0")
