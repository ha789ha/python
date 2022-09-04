import requests
from datetime import datetime

pixela_endpoint = " https://pixe.la/v1/users"
TOKEN = "nvsjn23smn"
USER_NAME = "hahava789"
GRAPH_ID = "graph1"

##user_endpoint
pixela_param = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_param)


## Graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_param = {
    "id":GRAPH_ID,
    "name":"cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

header = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_param, headers=header)


## post-pixel endpoint
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"


today = datetime.now()

post_param = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"5.2"

}
# response = requests.post(url=post_endpoint, json=post_param, headers=header)
# print(response.text)


## put method
update_enpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20220804"

update_param = {
    "quantity":"0"
}
#
# response = requests.put(url=update_enpoint, json=update_param, headers=header)
# print(response.text)


## Delete Method
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20220804"

response = requests.delete(url=delete_endpoint, headers=header)
print(response.text)