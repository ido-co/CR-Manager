import monday.rest as rest


# Returns a dictionary building_name -> building_id.
def get_buildings():
    return rest._get_buildings()


def get_timetable(building_name, room, day):
    return rest._get_timetable(building_name, room, day)


def get_building_idx_timetable(building_name):
    return rest._get_building_idx_timetable(building_name)

# Creates a task for building_id.
def create_task(building_id, room, title, desc, owner=None, urgency=None):
    return rest._create_task(building_id, room, title, desc, owner, urgency)





