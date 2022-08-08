from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timers = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timers)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text="Timer")
    check_mark.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text='Long Break', fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text='Worktime', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec == f'0{count_sec}'


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timers
        timers = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text='✓'*math.floor(reps/2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'),fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text='Start', command=start_timer)
start.grid(column=0, row=3)

reset = Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=3)

check_mark = Label(text='', fg=GREEN, bg=YELLOW, font=(30))
check_mark.grid(column=1, row=3)



window.mainloop()
