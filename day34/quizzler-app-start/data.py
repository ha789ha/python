import requests

parameters = {
    'type':'boolean',
    'amount':10
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()['results']

