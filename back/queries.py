import monday.api as api
from collections import defaultdict

ac_counter = defaultdict(int)

class BuildingError(Exception):
    pass


def open_ticket(building_name, room, title, desc, owner=None, urgency=None):
    # Refresh buildings and get id
    building_to_int = api.get_buildings()
    try:
        building_id = building_to_int[building_name]
    except KeyError:
        raise BuildingError
    try:
        api.create_task(building_id, room, title, desc, owner=None, urgency=None)
    except ConnectionError:
        raise ConnectionError
    return 0


def inc_ac_counter(room):
    ac_counter[room] += 1
    return ac_counter[room] > 0


def dec_ac_counter(room):
    ac_counter[room] -= 1
    return ac_counter[room] > 0


def reset_ac_counter():
    global ac_counter
    ac_counter = defaultdict(int)

