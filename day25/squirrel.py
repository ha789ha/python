import pandas as pd
data = pd.read_csv('squirrel.count.csv')
print(data[data['Primary Fur Color'] == 'Gray'].count())