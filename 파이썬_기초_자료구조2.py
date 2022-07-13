## 자료구조

from os import remove


파이썬의 자료구조에는 시퀀스가 있으며 파이썬은 6개의 내장 시퀀스가 있다(str, bytes, bytrrrary, list, tuple, dictionary)


# 튜플

리스트와 튜플은 매우 유사하지만 튜플은 변경이 불가능하다는 특징이 있다

fruit = () 이런 식으로 소괄호를 이용하여 생성한다

1. 튜플 <> 리스트

list = [1,2,3,4,5]
tuple1 = tuple(list)

2. 튜플의 덧셈

튜플은 기본적으로 더하는 것이 불가능하지만 += 연산자를 이용하면 가능하다

3. 튜플의 패킹, 언패킹

튜플은 하나의 변수 안에 여러가지 자료를 넣는 것과 같다. 따라서 이것을 다시 여러 변수로 나누어줄 수 있으며 이를 패킹이라 한다

x = ("apple", "banana", "grape")  
x = (s, q, z)  
s  

5. enumerate()

for 루프를 돌리면서 요소의 인덱스까지 알 수 있는 함수이다
x = ("apple", "banana", "grape")  
for index,value in enumerate(x) :  
    print(index, value)  

6. 우리는 왜 튜플을 이요할까?

- 코드의 처리가 간단해진다
- 딕셔너리의 키가 될 수 있다
- 다른 개발자가 변경하는 것을 금지할 때 사용할 수 있다

# 세트

수학에서 배우는 집합이라고 할 수 있으며 고유한 값들을 저장하는 자료구조

number = {1,2,3}  ## 중괄호를 이용해 감싸준다

1. 리스트에서 세트로의 변환

number = [1,2,3,1,2,3]
set1 = set(number) ## 세트는 집합이므로 중복요소는 제거한다

2. 공백세트

values = set()으로 공백세트를 만들어 줄 수 있다

3. 세트의 연산

## 세트 안에 있는 요소 검사

fruites = {"apple", "banna", "grape"}  

if "apple" in fruites :  
    print("사과가 있습니다")  

## 추가와 삭제

add(), remove(), 등등을 이용할 수 있다

6. 교집합, 차집합, 합집합

set1 = {1,2,3}  
set2 = {2,3,4}  
set3 = {3,4,5}  

set1 | set2 ## 합집합  
set1 & set2 ## 교집합  
set1 - set2 ## 차집합  

7. 리스트 <> 세트

리스트를 세트로 변환하면 집합의 성질을 이용하여 여러가지 성질들을 간단하게 처리할 수 있다


# 딕셔너리

딕셔너리는 각 값이 저마다 키를 갖고 있으며 이 키는 불변객체이다

capitals = {"korea":"seoul", "japan":"tokyo", "usa":"washigton"} ## 키 : 값

1. 항목탐색

딕셔너리에는 두가지의 요소가 존재하므로 키를 이용해 값을 찾을 수 있다.

2. 항목추가

capitals = {"korea":"seoul", "japan":"tokyo", "usa":"washigton"}

capitals["france"] = "paris"

## 딕셔너리 전체를 추가

capitals = {"korea":"seoul", "japan":"tokyo", "usa":"washigton"}

capitals2 = {"france":"paris"}

capitals.update(capitals2) ## update 함수를 이용한다

capitals

3. 딕셔너리의 함축

number = {x:x*x for x in range(100)}

4. 딕셔너리로 사전 만들기

phone = {}  
while (True) :  
    print("1. 연락처 추가")  
    print("2. 연락척 삭제")  
    print("3. 연락처 검색")  
    print("4. 연락처 출력")  
    print("5. 종료")  
    answer = int(input("메뉴 항목을 선택하세요"))  
    if answer == 1 :  
        a = input("추가할 연락처를 입력하세요")  
        b = input("누구의 연락처인가요?")  
        phone[b] = a  
    elif answer == 2 :  
        a = input("누구의 연락처를 삭제하고 싶으신가요")  
        phone.pop(a)  
    elif answer == 3 :  
        a = input("누구의 연락처를 찾고 싶으신가요?")  
        print(phone[a])  
    elif answer == 4 :  
        print(phone)  
    elif answer == 5 :  
        break  

## 딕셔너리에서는 item() 메서드를 이용하면 키와 값을 언패킹할 수 있다

score = {"kim" : [90, 83, 95], "lee" : [68, 45, 78], "choi" : [25, 56, 69]}  

for name, scores in score.items() :  
    print(name,"의 평균성적 =", sum(scores)/len(name) )  

