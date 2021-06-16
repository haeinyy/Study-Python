import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
# print(response.content) # content => body
soup = BeautifulSoup(response.content, 'html.parser') # <> 기준으로 파싱
# print(soup)

table = soup.find('table', {'class': 'table_develop3'})

data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    # print(tds, '\n')

    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperture = tds[5].text
            humidity = tds[9].text
            data.append([point,temperture,humidity])

print(data)