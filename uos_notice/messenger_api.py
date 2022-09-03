from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC3306113769342c8fd73505b3d4bdfe3c"
auth_token = "6aa0b35fc5102ed6b3432e50393a9c1f"
KEYWORD = '빅데이터'

def alarm_notice():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"{KEYWORD}가 포함된 공지가 올라왔습니다. 지금 확인하세요!",
        from_='+1 980 385 7686',
        to='+82 10 4934 5696'
    )
    print(message.status)
