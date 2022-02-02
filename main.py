import requests
from datetime import date as dt
USERNAME = "jellyredfox"
TOKEN = "hide"
GRAPH_ID = "graph2"

date = dt.today().strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": "yibnmnweiuhioewknekjugec",
    "username": "jellyredfox",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Book",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

point_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

point_config = {
    "date": date,
    "quantity": f"{input('How many time you read book? ')}"
}

response = requests.post(url=point_endpoint, json=point_config, headers=headers)
print(response.text)
# put_config = {
#     "quantity": "58"
# }
#
# # response = requests.put(url=f"{point_endpoint}/{date}", json=put_config, headers=headers)
# # print(response.text)
#
# delete_endpoint = 'https://pixe.la/v1/users/jellyredfox/graphs/graph1'
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response)