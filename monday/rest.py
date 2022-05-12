from datetime import datetime
import json
from types import SimpleNamespace
import utils


def _create_task(building_id, room, title, desc, owner=None, urgency=None):
    building_id = str(building_id)
    date = datetime.today().strftime('%Y-%m-%d')
    gql = utils.create_base.replace("__BUILDING_ID__", building_id)
    gql = gql.replace("__ROOM__", room)
    gql = gql.replace("__TITLE__", title)
    gql = gql.replace("__DESC__", desc)
    gql = gql.replace("__DATE__", date)

    return utils.do_gql(gql)


def _get_buildings():
    all_buildings_json = utils.do_gql(utils.get_buildings_base)
    all_buildings_raw = json.loads(all_buildings_json, object_hook=lambda x: SimpleNamespace(**x)).data.boards
    all_buildings = {}
    for ns in all_buildings_raw:
        all_buildings[ns.name] = ns.id

    return all_buildings

