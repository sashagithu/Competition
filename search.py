import requests
from bs4 import BeautifulSoup
request = "компьютер"
url = "https://ru.wikipedia.org/wiki/Special:Search?search=" + request
wikipedia = "https://ru.wikipedia.org"
r = requests.get(url)
k = r.text
k = k.encode("utf-8-sig")
f = open('index.html', 'wb').write(k)
soup = BeautifulSoup(k, 'html.parser')
try:
    title = str(soup.find('div', class_='searchresult').text)
    link = wikipedia + soup.find('div', class_='mw-search-result-heading').find_all('a')[0].get("href")
    answer = title + "... \n" + "Читать далее: \n" + link
    print(answer)
except AttributeError:
    answer = 'Ответ на запрос по ссылке: ' + wikipedia + '/wiki/' + request + '/'
    print(answer)
