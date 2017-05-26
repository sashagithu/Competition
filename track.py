import requests
from bs4 import BeautifulSoup
i = 0
tracker = 'RS534779941CN'
url = 'https://gdeposylka.ru/courier/china-post/tracking/' + tracker
r = requests.get(url)
k = r.text
k = k.encode("utf-8-sig")
f = open('index.html', 'wb').write(k)
soup = BeautifulSoup(k, 'html.parser')
div_stats = soup.find('li')
len2 = div_stats
len2 = len(len2)
while i != len2:
        date = soup.find('ul', class_='checkpoints').find_all('time', class_='datetime2')[i].get('datetime').split("T")[i]
        status = soup.find('ul', class_='checkpoints').find_all('strong', class_='checkpoint-status')[i].text
        place = soup.find('ul', class_='checkpoints').find_all('a')[i].text
        word1 = ' '.join((status).split())
        word2 = ' '.join((place).split())
        word3 = date
        i += 1
