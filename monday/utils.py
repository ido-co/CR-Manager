import requests

api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDE2OTc3MCwidWlkIjozMDQyMDk2MywiaWFkIjoiMjAyMi0wNS0xMlQwODoxMzozNC4x" \
          "NDhaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIxMzIwMjUsInJnbiI6InVzZTEifQ.T9k_B_wCAp-1O6Shnx1pLWf4Q9ZeWE" \
          "kUffDr4ryEDzo"


def do_gql(gql):
    response = requests.post(
    url="https://api.monday.com/v2/",
    headers={"Authorization": api_key, "Content-Type": "application/json"},
    json={"query": gql}
    )

    print(response.text)
