from flask import Flask, render_template, request, flash, redirect, url_for
from back.queries import open_ticket, inc_ac_counter, dec_ac_counter, get_classes ,get_building_idx_timetable

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('oops.html')


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
        url = url_for("classroom_ac_page", building="checkpoint", classroom=123)
        return redirect(url, code=302)

    return render_template('ac.html',
                           building=building,
                           room=classroom,
                           ac_status=("on" if AC_STATUS else "off")
                           )


@app.route('/<building>/<classroom>/ticket', methods=['GET', 'POST'])
def classroom_ticket_page(building, classroom):
    if request.method == 'GET' or assert_input(request.form,
                                               ["ticket_title", "ticket"]):
        return render_template('ticket.html',
                               building=building,
                               room=classroom,
                               )

    open_ticket(title=request.form["ticket_title"],
                desc=request.form["ticket"],
                urgency=int(request.form["urgency"]),
                building_name=building,
                room=classroom,
                )
    return render_template('ticket.html',
                           building=building,
                           room=classroom,
                           )


def assert_input(req, input_list):
    missing = False
    for item in input_list:
        if req.get(item) == '':
            flash(f"{item} is missing", category="error")
            missing = True
    return missing


if __name__ == '__main__':
    app.run(host="0.0.0.0")
