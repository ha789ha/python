import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for(index, row) in data.iterrows()}
print(data_dict)

word = input('Enter a word').upper()

answer_list = [data_dict[letter] for letter in word]
print(answer_list)