import monday.api as api
from collections import defaultdict
import datetime
from datetime import date
import calendar

ac_counter = defaultdict(lambda: [0, datetime.datetime.now()])

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
def inc_ac_counter(room):
    now = datetime.datetime.now()
    ac = ac_counter[room]
    if (now - ac[1]).seconds > 60:
        ac[1] = now
        ac[0] = 1
    else:
        ac[0] += 1
    return ac_counter[room][0] > 0


def dec_ac_counter(room):
    now = datetime.datetime.now()
    ac = ac_counter[room]
    if (now - ac[1]).seconds > 60:
        ac[1] = now
        ac[0] = -1
    else:
        ac[0] -= 1
    return ac_counter[room][0] > 0


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
