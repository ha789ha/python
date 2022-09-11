## 알고리즘의 예를 살펴보자
a = int(input())
b = int(input())
c = int(input())
maximum = a

if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

print(maximum)
'''이러한 구조를 선택구조라 하며 알고리즘의 간단한 예이다
따라서 알고리즘은 "어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차"라 할 수 있다'''


## 세 정수의 대소 관계와 중앙값

'1. 세 정수의 대소 관계 나열'
'위의 최대값을 찾는 알고리즘은 결정트리의 예이다.'

'2. 세 정수의 중앙값 구하기'
# 첫번째 방법
def med(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a >= c:
            return c
        else :
            return a
    elif b <= c:
        return b
    elif c > a:
        return c
    else:
        return a
print(med(5, 7, 2))

# 두번째 방법
if (a >= b and a <= c) or (a <= b and a >= c):
    medium = a
elif (a > b and c < b) or (a < b and b < c):
    medium = b
else :
    medium = c
print(medium)
'얼핏보면 두번째 방법이 코드는 적지만 한 번 비교했던 사항을 또 비교해야 하기 때문에 코드로써는 비효율적이다'

