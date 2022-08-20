import requests

api_key = "5940e5a80ef059a1fe890425d8f867ee"
lat = 51.51
lng = -0.13
parameter = {
    'lat': lat,
    'lon': lng,
    'appid': api_key,
    "exclude":"current,minuately,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
