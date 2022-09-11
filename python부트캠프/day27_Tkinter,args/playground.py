'''Arguments'''

# 고급인수
def number(a = 1, b = 2, c = 3):
    print(a + b + c)

number(b = 5) ## default 인수를 설정해놓은 상태에서 특정 변수만 바꾸고 싶을때

# *args
def add(*args):  # 길이 제한이 없으며 변수들은 튜플로 저장된다
    return sum(args)


print(add(3, 6, 23))

# **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add =3, multiply=5) ## 변수들이 딕셔너리로 저장된다

# **kwargs로 함수 만들기
class car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get('model')    # kw['model']과 같지만 model이 입력되지 않아도 오류를 반환하지 않는다

my_car = car(make = 'hyundae', model='genesis')
print(my_car.model)
