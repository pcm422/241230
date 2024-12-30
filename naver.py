import requests
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query='
keyword = input('검색어를 입력하세요: ')
url = base_url + keyword
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
results = soup.select('.view_wrap')

for i in results:
    result = i.select_one('.title_link').text
    link = i.select_one('.title_link')['href']
    writer = i.select_one('.name').text
    dsc = i.select_one('.dsc_link').text
    print(f"제목 : {result}")
    print(f"링크 : {link}")
    print(f"작성자 : {writer}")
    print(f"요약 : {dsc}")
    print('---------------------------------')