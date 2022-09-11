import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for(index, row) in data.iterrows()}
print(data_dict)

while True:
    try:
        word = input('Enter a word').upper()
        answer_list = [data_dict[letter] for letter in word]
    except KeyError:
        print('sorry, only letters in the alphabet please')
    else:
        print(answer_list)
        break
