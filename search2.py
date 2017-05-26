import requests
from bs4 import BeautifulSoup
request = "что делать при рвоте"
url = "https://lifehacker.ru/?s=" + "что делать при землетрясении"
r = requests.get(url)
k = r.text
k = k.encode("utf-8-sig")
f = open('index.html', 'wb').write(k)
soup = BeautifulSoup(k, 'html.parser')
url2 = soup.find('div', class_='social-likes social-likes-mobile-for-fixed').get("data-url")
print(url2)
r = requests.get(url2)
k = r.text
k = k.encode("utf-8-sig")
f = open('index2.html', 'wb').write(k)
soup = BeautifulSoup(k, 'html.parser')
try:
    ol = soup.find('ol').find_all('li')
    i = 0
    for li in ol:
        text = ol[i].text
        print(text)
        i += 1
except AttributeError:
    print("Введен неверный запрос")
    pass

#print(ul)
#<div class="social-likes social-likes-mobile-for-fixed" data-url="https://lifehacker.ru/2015/02/23/pishhevoe-otravlenie/"