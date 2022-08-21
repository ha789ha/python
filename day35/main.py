import requests
from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC3306113769342c8fd73505b3d4bdfe3c"
auth_token = "5e6c1a94bc1f2380db0221ece0d71508"

lat = 21
lng = 104
parameter = {
    'lat': lat,
    'lon': lng,
    'appid': api_key,
    'exclude': 'current, minutely, daily'
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data_hourly = response.json()['hourly']
weather_slice = weather_data_hourly[:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it's going to rain today remember to bring an ☂",
        from_='+1 980 385 7686',
        to='+82 10 4934 5696'
    )
    print(message.status)