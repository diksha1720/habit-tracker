import requests
from datetime import datetime
USERNAME = 'diksha'
TOKEN = 'fnbvbsajlkurgqvfmabdfs'
GRAPH_ID = 'graph'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "My Workout Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"

}

headers = {
    'X-USER-TOKEN': TOKEN
}
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

date = today.strftime("%Y%m%d")

update_endpoint = f"{pixel_endpoint}/{date}"

update_pixel = {
    "quantity": "30",
}

# response = requests.put(url=update_endpoint, json=update_pixel, headers=headers)
# print(response.text)

del_date = "20211230"

delete_endpoint = f"{pixel_endpoint}/{del_date}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)



