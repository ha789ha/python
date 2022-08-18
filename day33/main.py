import requests
from datetime import datetime
my_lat = 51.507351
my_long = -0.127758
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

print(sunrise, sunset)

time_now = datetime.now()
print(time_now.hour)













