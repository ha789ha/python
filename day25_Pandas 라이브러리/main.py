'''판다스에 대해서 알아보자'''
#
import pandas as  pd
#
data = pd.read_csv('weather_data.csv')
#
# 'series and DataFrame'
# print(data) # DataFrame
# print(data['temp']) # Series
#
# data_dict = data.to_dict() # DataFrame to Dictionary
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())

# '''get data in columns'''
# print(data.condition)
#
# '''get data in Row'''
# print(data[data.day == 'Monday']) # 어떤 열이 특정값과 일치하는지 보려면 행을 출력한다
# print(data[data.temp == data.temp.max()])
#
monday = data[data.day == 'Monday']
print(monday.condition)