# ## 1 - 1 turtle 그래픽 사용
# import  anothor_module
# print(anothor_module.variable)
#
# from turtle import  Turtle, Screen
# # 객체를 생성
# timmy = Turtle()
# # 실제 객체를 출력
# print(timmy)
# # 메소드를 출력
# timmy.shape('turtle')
# timmy.color('Blue')
# timmy.forward(100)
#
#
# my_screen = Screen()
# # 객체들의 속성을 출력
# print(my_screen.canvheight)
# # 스크린을 종료하느 조건을 만드는 메소드
# my_screen.exitonclick()

## 2 - 2 파이선 외부 패키지 사용

#1. pypi.org > 설치하고 싶은 패키지 선택 > setting에서 install packages

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('poketmon Name' , ['Pikatchu', 'squitle', 'chrmander'])
table.add_column('Type', ['Electronic', 'Water', 'Fire'])
table.align = 'l'
print(table)













