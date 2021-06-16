import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
from selenium import webdriver

path = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findWeeklyBoxOfficeList.do'
driver = webdriver.Chrome()
driver.get(path)
soup = BeautifulSoup(driver.page_source, 'html.parser') # <> 기준으로 파싱

tbody_list = ['tbody_0','tbody_166','tbody_315','tbody_496']
result = []

for body in tbody_list:
    tbody = soup.find('tbody', {'id': body})
    data= {}

    for tr in tbody.find_all('tr'):
        tds = list(tr.find_all('td'))
        rank = tds[0].text
        rank = rank.strip()
        name = tds[1].find('a').text
        data[rank] = name
    result.append(data)

for i in result:
    print(i)