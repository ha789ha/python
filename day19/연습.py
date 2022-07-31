def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def cal(n1, n2, func):   ## 이런 식으로 다른 함수를 인자로 쓰는 것을 고차함수라 부른다
    return func(n1, n2)

print(cal(2, 3, add))
