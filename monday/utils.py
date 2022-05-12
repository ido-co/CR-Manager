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
        column_values: "{\\"text\\":\\"__DESC__\\",\\"text1\\":\\"__ROOM__\\",\\"status\\":\\"Open\\", \\"date4\\" :{\\"date\\" : \\"__DATE__\\"}}",
        ) {
        id
    }
}
"""

# GET ALL BUILDINGS AQL
get_buildings_base = "{ boards (limit:1000) { name id } }"

# DO A GQL REQUEST
def do_gql(gql):
    response = requests.post(
        url="https://api.monday.com/v2/",
        headers={"Authorization": api_key, "Content-Type": "application/json"},
        json={"query": gql}
    )

    print(response.text)
    return response.text
