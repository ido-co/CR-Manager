import monday.api as api
from collections import defaultdict
import datetime
from datetime import date
import calendar

ac_counter = defaultdict(lambda: [{}, datetime.datetime.now().hour])

class BuildingError(Exception):
    pass


##########
# TICKETS
##########
def open_ticket(building_name, room, title, desc, owner=None, urgency=None):
    # Refresh buildings and get id
    building_to_int = api.get_buildings()
    try:
        building_id = building_to_int[building_name]
    except KeyError:
        raise BuildingError
    try:
        api.create_task(building_id, room, title, desc, owner, urgency)
    except ConnectionError:
        raise ConnectionError
    return 0


#####
# AC
#####
def inc_ac_counter(room, ip):
    ac = ac_counter[room]
    zero_if_needed(ac)
    ac[ip] = 1
    return sum_ac(ac) > 0


def dec_ac_counter(room, ip):
    ac = ac_counter[room]
    zero_if_needed(ac)
    ac[ip] = -1
    return sum_ac(ac) > 0


def zero_if_needed(ac):
    now = datetime.datetime.now().hour
    if now != ac[1]:
        ac[0] = {}
    return


def sum_ac(ac):
    res = 0
    for key, val in ac:
        res += val
    return res


############
# TIMETABLE
############
def get_classes(building_name, room):
    curr_date = date.today()
    day = calendar.day_name[curr_date.weekday()]
    hour = str(datetime.datetime.now().hour) + "00"
    next_hour = str(datetime.datetime.now().hour + 1) + "00"
    timetable = api.get_timetable(building_name, room, day)

    return get_lesson(timetable, hour), get_lesson(timetable, next_hour)


def get_lesson(timetable, hour):
    NOTHING = f"Nothing ({hour})"
    if hour not in timetable:
        return NOTHING
    lesson = timetable[hour]
    if lesson:
        return f"{lesson} ({hour})"
