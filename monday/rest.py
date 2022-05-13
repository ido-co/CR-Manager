from datetime import datetime
import json
from types import SimpleNamespace
import monday.utils as utils


def _create_task(building_id, room, title, desc, owner=None, urgency=None):
    building_id = str(building_id)
    date = datetime.today().strftime('%Y-%m-%d')
    urgency = utils.get_urgency(urgency)
    gql = utils.create_base.replace("__BUILDING_ID__", building_id)
    gql = gql.replace("__ROOM__", room)
    gql = gql.replace("__TITLE__", title)
    gql = gql.replace("__DESC__", desc)
    gql = gql.replace("__DATE__", date)
    gql = gql.replace("__URGENCY__", urgency)

    return utils.do_gql(gql)


def _get_buildings():
    all_buildings = _get_buildings_generic(utils.get_buildings_base)
    return all_buildings


def _get_timetable_buildings():
    all_buildings = _get_buildings_generic(utils.get_timetable_buildings_base)
    return all_buildings


def _get_buildings_generic(gql_base):
    all_buildings_json = utils.do_gql(gql_base)
    all_buildings_raw = json.loads(all_buildings_json, object_hook=lambda x: SimpleNamespace(**x)).data.boards
    all_buildings = {}
    for ns in all_buildings_raw:
        all_buildings[str(ns.name).lower()] = ns.id

    return all_buildings


def _get_building_timetable(building_name):
    building_id = _get_building_idx_timetable(building_name)
    timetable_gql = utils.get_timetable_base.replace("__BUILDING_ID__", building_id)
    return utils.do_gql(timetable_gql)


def _get_building_idx_timetable(building_name):
    building_map = _get_timetable_buildings()
    print(building_name)
    print(building_map)
    if building_name.strip() not in building_map.keys():
        raise ValueError

    return building_map[building_name]


def _get_timetable(building_id, room, day):
    full_timetable_json = _get_building_timetable(building_id)
    full_timetable = json.loads(full_timetable_json, object_hook=lambda x: SimpleNamespace(**x)).data.boards

    timetable = {}
    try:
        for ns in full_timetable:
            for r in ns.items:
                if r.name == day and r.group.title == room:
                    for hour in r.column_values:
                        timetable[hour.title] = hour.value
    except:
        ValueError

    return timetable

