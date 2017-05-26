import telebot
import cfg
import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2

bot = telebot.TeleBot(cfg.token)

upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Добрый день участники и жюри конкурса! Это наш проект, бот в меседжере Telegram!")

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который был создан для представления способностей команды")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == "а":
        bot.send_message(message.chat.id, "буква а")
    elif message.text.lower() == "б":
        bot.send_message(message.chat.id, "буква б")
    elif message.text == 'фото':
        url = 'https://pp.userapi.com/c636216/v636216706/3301c/3PDy6wA37_g.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text.lower().split(' ')[0] == 'что':
        print(message.text.lower())
        #request = "что делать при отравлении"
        request = message.text.lower()
        url = "https://lifehacker.ru/?s=" + request
        r = requests.get(url)
        k = r.text
        k = k.encode("utf-8-sig")
        f = open('index.html', 'wb').write(k)
        soup = BeautifulSoup(k, 'html.parser')
        url2 = soup.find('div', class_='social-likes social-likes-mobile-for-fixed').get("data-url")
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
                bot.send_message(message.chat.id, text)
                i += 1
        except AttributeError:
            text = 'Введен неверный запрос'
            bot.send_message(message.chat.id, text)
            pass

    else:
        request = message.text.lower()
        bot.send_message(message.chat.id, search(request))

def search(request):
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
    except AttributeError:
        answer = 'Ответ на запрос по ссылке: ' + wikipedia + '/wiki/' + request + '/'
    return answer





bot.polling(none_stop=True, interval=0)

