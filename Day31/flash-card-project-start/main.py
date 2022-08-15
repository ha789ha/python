import random
from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv('data/french_words.csv')
dict_data = data.to_dict(orient="records") #orient로 딕셔너리를 변환하는 방식을 정해줄 수 있다

#-----------------func---------------------

def click_button():
    global current_card
    current_card = random.choice(dict_data)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(text_word, text=current_card['French'])
    canvas.itemconfig(title_word, text='French')
    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(text_word, text=current_card['English'])
    canvas.itemconfig(title_word, text='English')







#-----------------class---------------------

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_img = canvas.create_image(400, 263, image=card_front_img)
text_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
title_word = canvas.create_text(400, 150, text='Title', font=('Ariel', 48, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image,highlightthickness=0, command=click_button)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=click_button)
known_button.grid(row=1, column=1)




window.mainloop()