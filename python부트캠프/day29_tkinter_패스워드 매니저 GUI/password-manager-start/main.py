from tkinter import *
from tkinter import messagebox
FONT_NAME = "Courier"


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f'these are detail entered:\nemail: {email}'
                                                  f'\npassword : {password}\nis it okay to save?')

    if is_ok:
        with open('data.txt', 'a') as data_file:
            data_file.write(f'{website} | {email} | {password} \n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100,  image=logo_img)
canvas.grid(column=1, row=0)

input_website = Label(text='Website:',font=(FONT_NAME, 10, 'bold'))
input_website.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

input_email = Label(text='Email/Username:', font=(FONT_NAME, 10, 'bold'))
input_email.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, '789ha@naver.com')

input_password = Label(text='Password:', font=(FONT_NAME, 10, 'bold'))
input_password.grid(column=0, row=3)
password_entry = Entry(width=15)
password_entry.grid(column=1, row=3)

gen_password = Button(text='Generate Password', width=14)
gen_password.grid(column=2, row=3)

add = Button(text='add', width=35, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()