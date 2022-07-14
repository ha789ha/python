## 문자열

from subprocess import STARTF_USESHOWWINDOW


1. 대소문자 변환(capitalize)

s = "item"
s.capitalize()

2. 찾기 및 바꾸기

# startswith

# endwith

# replace
a = "python"
a.replace("p", "a")

# find()
a = "python"
a.find("p")  ## 함수가 포함하는 문자열의 인덱스 반환, 없을 경우 -1 반환

# count()
a.count("p")

## 이들 메소드는 시작, 끝 위치를 정할 수 있다 (인수, 시작, 종료)

# isalpha() 모두 알파벳이면 true 변환

# islower() 모두 대문자면 true 반환

# strip() 공백제거

# split() 문자열을 분해(기본적으로는 공백으로 문자를 구분하며 원하는 구분자를 설정해줄 수 있다)

# 문자열을 문자로 분해하려면 리스트 선언을 해주면 된다

