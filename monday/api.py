import monday.rest as rest


# Returns a dictionary building_name -> building_id.
def get_buildings():
    return rest._get_buildings()


def get_timetable(building_name, room, day):
    return rest._get_timetable(building_name, room, day)


# Creates a task for building_id.
def create_task(building_id, room, title, desc, owner=None, urgency=None):
    return rest._create_task(building_id, room, title, desc, owner, urgency)





