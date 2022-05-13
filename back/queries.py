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
    ac[0][ip] = 1
    return sum_ac(ac) > 0


def dec_ac_counter(room, ip):
    ac = ac_counter[room]
    zero_if_needed(ac)
    ac[0][ip] = -1
    return sum_ac(ac) > 0


def zero_if_needed(ac):
    now = datetime.datetime.now().hour
    if now != ac[1]:
        ac[0] = {}
    return


def sum_ac(ac):
    res = 0
    for key, val in ac[0].items():
        res += val
    return res


############
# TIMETABLE
############
def format_time(hour):
    return f"0{hour}00" if len(hour) == 1 else f"{hour}00"


def get_classes(building_name, room):
    curr_date = date.today()
    day = calendar.day_name[curr_date.weekday()]

    hour = format_time(str(datetime.datetime.now().hour))
    next_hour = format_time(str((datetime.datetime.now().hour + 1) % 24))
    timetable = api.get_timetable(building_name, room, day)

    return get_lesson(timetable, hour), get_lesson(timetable, next_hour)


def get_lesson(timetable, hour):
    """
    for internal use
    do not call
    """
    NOTHING = f"Nothing ({hour})"
    if hour not in timetable:
        return NOTHING
    lesson = timetable[hour]
    if lesson:
        return f"{lesson} ({hour})"


def get_building_idx_timetable(building):
    return api.get_building_idx_timetable(building.lower())