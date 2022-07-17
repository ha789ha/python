## 객체와 클래스

프로그래밍은 크게 객체지향과 절차지향으로 나눌 수 있다

파이썬은 대표적인 객체지향 프로그래밍, 파이썬에서는 모든 것이 객체이다

따라서 객체, 클래스라는 개념을 잘 숙지할 필요가 있다

차로 비유를 들면 클래스는 차의 설계도라 할 수 있으며 브랜드들은 객체라 할 수 있다

# 클래스

1. 작성

class counter :
    def __init__(self) :
        self.count = 0
    def increment(self) :
        self.count += 1   ## 클래스 안에 변수와 함수를 정의하며 이 때 변수를 인스턴스 변수, 안의 함수를 메소드라 한다

a = counter(초기값 설정)  ## counter 클래스 호출
a.increment()  ## 클래스의 incerment 호출
a.increment()
a.__init__()   ## 클래스의 __init__ 호출
print(a.count)

a = counter(100)
b = counter(0)  # 우리는 하나의 클래스로 여러가지 객체(a,b)를 만들 수 있다

## 채널, 볼륨, 전원을 변수로 티비라는 클래스를 만들어보자
class tv :
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self) :
        print(self.channel, self.volume, self.on)
    
    def setChannel(self, channel) :
        self.channel = channel
        
    def getChannel(self) :
        return self.channel
    
t = tv(7, 9, True)
t.setChannel(1)
t.getChannel()

## 원의 길이, 둘레 등을 구하는 클래스를 만들어보자

class circle :
    def __init__(self, radious = 0) :
        self.radious = radious
    
    def getArea(self) :
        return self.radious**2*3.14
    
    def getPrimeter(self) :
        return self.radious*2*3.14

2. 객체참조

t = class()라 할때 변수 t는 객체의 주소를 저장하고 있는 것이지 객체 자제를 저장하는 것이 아니다.

c = circle(15)
a = c  ## 따라서 이런 식으로 변수를 복사해주면 a는 c와 동일한 객체를 가르킨다

if a is c :
    print("hi")  ## 두 변수가 동일한 객체를 가르킬 때 이 연산자를 쓸 수 있다

# none 참조
변수가 현재 아무것도 가르키지 않는다면 none으로 설정하는 것이 좋다

3. 클래스 변수

클래스 안의 변수는 인스턴스 변수와 클래스 변수가 있으며 클래스 변수는 모든 객체가 참조할 수 있는 변수이다.

class tv :
    serialNumber = 0  # 클래스 변수를 정의
    
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        tv.serialNumber += 1
        self.number = tv.serialNumber # 클래스 변수 조정
        
    def show(self) :
        print(self.channel, self.volume, self.on, self.number)
        
mytv = tv(15, 10, True)
mytv.show()

# 상수 클래스 변수

class monster :
    weak = 0
    normal = 10
    strong = 20
    very_strong = 30
    
    def __init__(self) :
        self._health = monster.normal
        
    def eat (self) :
        self._health = monster.strong
        return self._health
        
    def attack (self) :
        self._health = monster.weak
        
me = monster()0
me.eat()  ## 상수 클래스 변수는 초기값을 설정할떄 유용하다

## 우리는 언제 클래스 변수를 사용할까??
예를 들어 섬에 강아지들이 살고 있는데 품종이 모두 동일하다고 가정하자 그렇다면 품종은 클래스 변수로 설정하여 모든 객체가 
공유하도록 할 수 있다

4. 특수 메소드

