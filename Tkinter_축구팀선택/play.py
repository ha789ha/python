import tkinter.font
from tkinter import *
import data
import pandas as pd
import requests
team_stat = data.stats
class TeamStats:

    def __init__(self):
        self.window = Tk()
        self.window.title('soccer game')
        self.window.config(bg='white', padx=10, pady=10)

        che_image = PhotoImage(file='img/che.jpg')
        self.che_button = Button(image=che_image, highlightthickness=0, bg='white', bd=0, command=lambda : self.click_team("Chelsea"), text="Chelsea")
        self.che_button.grid(row=0, column=0, pady=10, padx=10)

        tot_image = PhotoImage(file='img/tot.png')
        self.tot_button = Button(image=tot_image, highlightthickness=0, bg='white', bd=0, command= lambda :self.click_team('Tottenham Hotspur'), text="Tottenham Hotspur")
        self.tot_button.grid(row=1, column=0, pady=50, padx=50)

        mcu_image = PhotoImage(file='img/mcu.png')
        self.mcu_button = Button(image=mcu_image, highlightthickness=0, bg='white', bd=0, command=lambda :self.click_team("Manchester United"), text="Manchester United")
        self.mcu_button.grid(row=1, column=1, pady=50, padx=50)

        mnc_image = PhotoImage(file='img/mnc.png')
        self.mnc_button = Button(image=mnc_image, highlightthickness=0, bg='white', bd=0, command=lambda :self.click_team("Manchester City"), text="Manchester City")
        self.mnc_button.grid(row=0, column=1, pady=50, padx=50)

        self.window.mainloop()


    def click_team(self, text):
        self.window.destroy()
        self.window = Tk()
        self.window.title('soccer game')
        self.window.config(bg='white', padx=10, pady=10)
        self.team = text
        self.season_list = []
        for i in range(12):
            if i < 5:
                self.choose_season = Button(text=f'200{i + 5}-200{i + 6}', bd=0, command=lambda i=i :self.click_season(f'200{i + 5}-200{i + 6}'))
                self.choose_season.grid(row=i, column=1, pady=20, padx=20)
                self.season_list.append(self.choose_season)
            else:
                self.choose_season = Button(text=f'20{i + 5}-20{i + 6}', bd=0, command=lambda i=i :self.click_season(f'20{i + 5}-20{i + 6}'))
                self.choose_season.grid(row=i - 5, column=2, pady=20, padx=20)
                self.season_list.append(self.choose_season)


        self.window.mainloop()

    def click_season(self, text):
        self.window.destroy()
        self.window = Tk()
        self.window.title('soccer game')
        self.window.config(bg='white', padx=30, pady=30)
        self.season = text

        self.summory = Label(text = f"{self.team}'s perfomance in the {self.season} seaseon", font=('concolas', 30), bg='white')
        self.summory.grid(row=0, column=0, pady=30, padx=20)

        self.count_wins = team_stat.loc[(team_stat['team'] == self.team) & (team_stat['season'] == self.season), ['wins']].values[0]
        self.wins = Label(text = f'{self.team} 승리 : {self.count_wins}', font=('concolas', 20), bg='white')
        self.wins.grid(row=1, column=0, pady=20, padx=20)

        self.count_losses = team_stat.loc[(team_stat['team'] == self.team) & (team_stat['season'] == self.season), ['losses']].values[0]
        self.losses = Label(text=f'{self.team} 패배 : {self.count_losses}', font=('concolas', 20), bg='white')
        self.losses.grid(row=2, column=0, pady=20, padx=20)

        self.count_goals = team_stat.loc[(team_stat['team'] == self.team) & (team_stat['season'] == self.season), ['goals']].values[0]
        self.goals = Label(text=f'{self.team} 득점 : {self.count_goals}', font=('concolas', 20), bg='white' )
        self.goals.grid(row=4, column=0, pady=20, padx=20)

        self.draws = Label(text=f'{self.team} 무승부 : {38 - (self.count_wins + self.count_losses)}', font=('concolas', 20), bg='white')
        self.draws.grid(row=3, column=0, pady=20, padx=20)


TeamStats()
















