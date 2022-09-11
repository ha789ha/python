import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzelr')
        self.window.config(bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text='ji', fill=THEME_COLOR)

        check_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.text = Label(text=f'score = {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.text.grid(row=0, column=1, pady=20)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.text.config(text=f'score = {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='the end')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))




    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
