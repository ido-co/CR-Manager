import rest


# Returns a dictionary building_name -> building_id.
def get_buildings():
    return rest._get_buildings()


# Creates a task for building_id.
def create_task(building_id, room, title, desc, owner=None, urgency=None):
    return rest._create_task(building_id, room, title, desc, owner, urgency)





