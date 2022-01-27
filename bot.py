import config
import telebot
import time
import requests
import bs4

tok = config.token
bot = telebot.TeleBot(tok)
url = 'https://www.anekdot.ru/random/'


def getanekdot():
    z=''
    s=requests.get('http://anekdotme.ru/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.anekdot_text')
    for x in p:        
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '👌Привет! Это бот который отправляет тебе анекдоты! Пробуй!🥳 \n Жми сюда что бы узнать больше --> /help ')



@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, 'Бот работает очень просто! Нажимаешь сюда --> /anekdot \n и бот отправляет анекдот! Пользуйся!🥳')


@bot.message_handler(commands=['anekdot'])
def anekdot(message):
	 bot.send_message(message.from_user.id, getanekdot())
@bot.message_handler(content_types=['text'])
def send(message):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all(id="a_rnd")
	for quote in quotes:
		anegdot = quote.text
		print(quote.text)
		bot.send_message(message.chat.id, anegdot)


bot.polling(none_stop=True)