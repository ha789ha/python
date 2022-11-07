from bs4 import BeautifulSoup

with open('website.html', 'rt', encoding='UTF8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser") # html을 읽는 방식을 정해줘야 하는데 html.parser가 인식되지 않는 경우 lxml 사용

print(soup.title) # title 객체를 가져옴
print(soup.title.string) # title의 내용을 가져옴
print(soup.prettify()) # 내용 전체를 가져옴

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText()) # a 태그 안에 있는 모든 내용을 가져올 수 있음
    print(tag.get('href')) # a 태그 안에 있는 링크들을 가져올 수 있음

heading = soup.find(name='h1', id='name') # find 함수를 쓰면 첫번째 태그만 가져온다
print(heading)

section_heading = soup.find(name='h3',class_='heading')
print(section_heading.getText())

company_url = soup.select_one(selector="p a") # p 안에 있는 a 태그를 선택
print(company_url)

print(soup.select(".heading"))