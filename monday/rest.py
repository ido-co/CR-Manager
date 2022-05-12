import utils


def _create_task(building_id, room, desc, owner=None, urgency=None):
    gql = 'mutation { ' \
            'create_item(' \
                'board_id: ' + str(building_id) + ', ' \
                'group_id: "topics", ' \
                'item_name: "' + desc + '"), ' \
                'column_values: "{"room_no_5":"1234","status":"Open", "date4" : {"date" : "2022-05-12"}}"' \
            '{id}}'

    utils.do_gql(gql)


def _get_buildings():
    return {"checkpoint": 2663304427, "gilman": 2663320712}


def _get_rooms(building_id):
    return ["001", "002", "101", "102", "201", "202"]
