'''list comprehension'''
# 제곱수 구하기
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# 겹치는 데이터 제거
a = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
b = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

common_number = [number for number in a if number in b]
print(common_number)
`
import pandas

'''dictionary comprehension'''
# 문자열을 구분하고 그 문자열의 길이를 반환하는 딕셔너리 생성
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
my_list = sentence.split(' ')
result = {i:len(i) for i in my_list }
print(result)

# 섭씨온도를 화씨온도로 변환
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    key:(value*9/5) + 32 for (key, value) in weather_c.items()
}
print(weather_f)

'''DataFrame comprehension'''
student_dict = {
    'student': ['Angela', 'James', 'Lilly'],
    'score' : [56, 78, 89]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    print(row.student) # or print(row or index)
