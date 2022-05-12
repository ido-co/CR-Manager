import monday.api as api

Building_to_int = None


class BuildingError(Exception):
    pass


def open_ticket(building_name, room, desc, owner=None, urgency=None):
    # Refresh buildings and get id
    global Building_to_int
    Building_to_int = api.get_buildings()
    try:
        building_id = Building_to_int[building_name]
    except KeyError:
        raise BuildingError

    api.create_task(building_id, room, desc, owner=None, urgency=None)

