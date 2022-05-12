import rest


def get_buildings():
    return rest._get_buildings()


def get_rooms(building_id):
    return rest._get_rooms(building_id)


def create_task(building_id, room, desc, owner=None, urgency=None):
    return rest._create_task(building_id, room, desc, owner, urgency)





