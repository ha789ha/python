# IndexError 처리
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")


make_pie(4)

# KeyError 처리
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0  # pass를 쓰는 것이 더 간편

print(total_likes)

# Nato Alphabet Game 예외처리
import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for(index, row) in data.iterrows()}
print(data_dict)

def Nato():
    try:
        word = input('Enter a word').upper()
        answer_list = [data_dict[letter] for letter in word]
    except KeyError:
        print('sorry, only letters in the alphabet please')
        Nato()
    else:
        print(answer_list)
        break

Nato()