import requests

# MONDAY API KEY (SECRET!)
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE2OTc3MCwidWlkIjozMDQyMDk2MywiaWFkIjoiMjAyMi0wNS0xMlQwODoxMzozNC4x" \
          "NDhaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIxMzIwMjUsInJnbiI6InVzZTEifQ.T9k_B_wCAp-1O6Shnx1pLWf4Q9ZeWE" \
          "kUffDr4ryEDzo"

# CREATE TASK BASE GQL
create_base = """mutation {
    create_item (
        board_id: __BUILDING_ID__,
        group_id: "topics",
        item_name: "__TITLE__",
        column_values: "{\\"text\\":\\"__DESC__\\",\\"text1\\":\\"__ROOM__\\",\\"status\\":\\"Open\\", \\"status_1\\":\\"__URGENCY__\\", \\"date4\\" :{\\"date\\" : \\"__DATE__\\"}}",
        ) {
        id
    }
}
"""

# GET TIMETABLE BASE GQL
get_timetable_base = """query {
  boards (ids: __BUILDING_ID__) {
    items {
      name
      group {
          title
      }
      column_values {
        title
        value
      }
    }
  }
}
"""

# GET ALL BUILDINGS AQL
get_buildings_base = "{ boards (limit:1000, board_kind: private) {id name} }"
get_timetable_buildings_base = "{ boards (limit:1000, board_kind: public) {id name} }"

# DO A GQL REQUEST
def do_gql(gql):
    response = requests.post(
        url="https://api.monday.com/v2/",
        headers={"Authorization": api_key, "Content-Type": "application/json"},
        json={"query": gql}
    )

    if response.status_code >= 300:
        raise ConnectionError

    # print(response.text)
    return response.text


# GET URGENCY STRING FROM INT
def get_urgency(urgency_int):
    if urgency_int == 1:
        return "Very Low"
    if urgency_int == 2:
        return "Low"
    if urgency_int == 3:
        return "Medium"
    if urgency_int == 4:
        return "High"
    if urgency_int == 5:
        return "Critical"
    raise ValueError
