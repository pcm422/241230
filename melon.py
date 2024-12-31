import requests
from bs4 import BeautifulSoup

header_user = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://www.melon.com/chart/index.htm'

rep = requests.get(url, headers=header_user)
html = rep.text
soup = BeautifulSoup(html, 'html.parser')
lst50 = soup.select('.lst50')
lst100 = soup.select('.lst100')
lst_all = lst50 + lst100

for i in lst_all:
    rank = i.select_one('.rank').text
    title = i.select_one('.ellipsis.rank01 span a').text
    singer = i.select_one('.ellipsis.rank02 a').text
    album = i.select_one('.ellipsis.rank03 a').text
    print(f"순위 : {rank}")
    print(f"제목 : {title}")
    print(f"가수 : {singer}")
    print(f"앨범 : {album}")
    print('--------------------------------------------------')