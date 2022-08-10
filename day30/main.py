'''Example of exceptions'''

#FileNotFound
with open('a_file.txt') as file:
    file.read()

#KeyError
a = {'key' : 'value'}
a['not_exist']

#IndexError
fruit = ['apple', 'banana']
fruit[3]

#TypeError
text = 'abc'
print(text + 5)

'''Catching Exceptions'''

try:
    file = open('a_file.txt')  # 예외가 발생할 수 있는 코드 작성
    a = {'key' : 'value'}
    a['not_exist']
except FileNotFoundError:
    open('a_file.txt', 'w')  # 예외가 발생했을 경우 대안 마련(이 파일이 존재하지 않을 경우 생성)
except KeyError as error_message:             # 인자를 넣어주어 예외 포착을 할 수 있다
    print(f'the key {error_message} not found')
else:                        # 예외가 해결됐을 경우 실행
    content = file.read()
    print(content)
finally:                     # 예외의 발생여부에 관계 없이 실행된다
    raise TypeError('this is error i made up')  # raise를 이용하여 자신만의 에러를 발생시킬 수 있다

'''나만의 예외 발생'''

height = float(input('Height = '))
weight = int(input('Weight = '))

if height > 3:
    raise ValueError('height should not be over 3 meters.')

bmi = weight / height ** 2
print(bmi)