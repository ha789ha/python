from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

## 기사의 기사 헤드라인과 내용 뽑아내기
a = soup.find_all(name='span', class_='titleline')
article_texts = []
article_links = []
article_upvotes = []

for i in a:
    article_text = i.contents[0].text
    article_link = i.contents[0].get('href')
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvote = soup.find_all(name='span', class_='score')
for i in article_upvote:
    article_upvotes.append(int(i.text.split()[0]))

max_vote = article_upvotes.index(max(article_upvotes))
print(article_texts[max_vote])
print(article_links[max_vote])