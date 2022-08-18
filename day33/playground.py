import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code) # response 200이라는 메세지가 뜸
if response.status_code != 200:
    raise Exception('Bad response from ISS API')
response.raise_for_status()

## HTTP 상태 코드
# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go Away(권한 없음)
# 4XX: You Screwed Up(존재하지 않음, 404 Not Found가 대표적인 예)
# 5XX: I Scrwed up(서버가 잘못되거나 다운)

