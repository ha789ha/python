'''use tkinter and make a gui'''
import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='I am a Label',font=('Arial', 24, "bold"))
my_label['text'] = 'New text'
my_label.config(text='New text') ## 이런 식으로 text인자를 바꿔줄 수 있다
my_label.grid(column=1, row=1)

# Button

def ButtonClick():
    answer = input.get()
    my_label['text'] = answer

button = tkinter.Button(text= "click me", command=ButtonClick)
button.grid(column=2, row=2)

new_button = tkinter.Button(text='newbutton')
new_button.grid(column=3, row=1)
# Entry

input = tkinter.Entry(width=10)
input.grid(column=4, row=3)







window.mainloop()