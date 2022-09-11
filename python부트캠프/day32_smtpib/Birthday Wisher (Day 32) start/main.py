import smtplib


connection = smtplib.SMTP("smtp.gamil.com", 587)
connection.starttls()    # 연결을 안전하게 만들기
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs= "smtp.naver.com", msg = "Hello")
connection.close()