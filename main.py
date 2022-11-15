import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import os
from dotenv import load_dotenv, find_dotenv

import telebot

from markup import kb, kb_shop, kb_smartphones, kb_accessories, kb_modems, kb1

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('token'))

urls = ['https://life.com.by/store/smartphones', 'https://life.com.by/store/accessories',
        'https://life.com.by/store/modems']
consultant = ['Елена', 'Ольга', 'Виктория', 'Олег']
name = choice(consultant)


def parse(url):
    r = requests.get(url)
    # print(r.status_code)
    sleep(1)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('a', class_='product-card')

    while True:
        text = ''
        if len(items):
            for item in items:
                model = getattr(item.find('div', class_='product-card__title'), 'text', None)
                price = getattr(item.find('span', class_='nobr product-card__footer-text-button'), 'text', None)
                text += f'{model}' + ' ' + f'{price}' + '\n'
        return text


parse(urls[0])
parse(urls[1])
parse(urls[2])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Здравствуй, уважаемый абонент, %s! Приветствую тебя в нашем помощнике!'
                                           'Чем могу помочь?' % message.from_user.full_name, reply_markup=kb)


@bot.message_handler(content_types=['text'])
def text_types(message):
    if message.text == 'привет' or message.text == 'Привет':
        bot.send_message(message.chat.id, text=message.text)

    if message.text == 'помощь' or message.text == 'Помощь':
        img = open('consult.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=img, caption=f'Здравствуйте, меня зовут {name}. Чем могу помочь?',
                       reply_markup=kb1)

    if message.text == 'покупка' or message.text == 'Покупка':
        bot.send_message(message.chat.id, text='Выберите одну из категорий', reply_markup=kb_shop)


@bot.callback_query_handler(func=lambda call: True)
def call_inline(call):
    if call.data == 'shop':
        bot.send_message(call.message.chat.id, text='Выберите одну из категорий', reply_markup=kb_shop)

    if call.data == 'help':
        img = open('consult.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=img, caption=f'Здравствуйте, меня зовут {name}. Чем могу помочь?',
                       reply_markup=kb1)

    if call.data == 'smartphones':
        bot.send_message(call.message.chat.id, parse(urls[0]))
        bot.send_message(call.message.chat.id, text='Хотите перейти к другим товарам или получить консультацию?',
                         reply_markup=kb_smartphones)

    if call.data == 'accessories':
        bot.send_message(call.message.chat.id, parse(urls[1]))
        bot.send_message(call.message.chat.id, text='Хотите перейти к другим товарам или получить консультацию?',
                         reply_markup=kb_accessories)

    if call.data == 'modems':
        bot.send_message(call.message.chat.id, parse(urls[2]))
        bot.send_message(call.message.chat.id, text='Хотите перейти к другим товарам или получить консультацию?',
                         reply_markup=kb_modems)


bot.polling(none_stop=True)
