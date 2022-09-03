# libraray
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
from messenger_api import alarm_notice

# variable name
KEYWORD = '빅데이터'

class GetTitleData:
    def __init__(self):
        self.page_html = urlopen(url="https://www.uos.ac.kr/korNotice/list.do?list_id=FA2&epTicket=LOG")
        self.data = BeautifulSoup(self.page_html, "html.parser")


    def make_title_list(self):
        self.notice = self.data.body.find_all('span', {'class': 'cl'})
        self.first_title = self.notice[-1].parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.a.text


    def check_newtitle(self):
        self.make_title_list()

        while True:
            time.sleep(60)
            response = urlopen(url="https://www.uos.ac.kr/korNotice/list.do?list_id=FA2&epTicket=LOG")
            data = BeautifulSoup(response, "html.parser")
            self.new_notice = data.body.find_all('span', {'class': 'cl'})
            self.new_first_title = self.notice[-1].parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.a.text
            if (self.new_first_title != self.first_title) and (KEYWORD in self.new_first_title) :
                print(self.new_first_title)
                alarm_notice()
                self.first_title = self.new_first_title


