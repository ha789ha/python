import smtplib
import requests
from datetime import datetime
import time

my_lat = 51.507351
my_long = -0.127758
my_email = "himy123454@gmail.com"
password = "jvlxslptnsovtsru"

def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if (my_lat - 5) <= (my_lat + 5)and (my_long - 5) <= (my_long + 5):
        return True


def check_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0
    }
    response_me = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response_me.raise_for_status()
    data_me = response_me.json()
    sunrise = int(data_me['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data_me['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if sunset <= time_now or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if check_night() and check_position():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg='subject:lokk up!\n\nthe ISS is above you in teh sky!'
        )

















