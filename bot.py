#!/usr/bin/env python
import telebot
import random
from telebot.types import Message


TOKEN = '986187862:AAEI7ewpt6nwCJZHxfAKQVEPuJBOZ733O4Q'

bot = telebot.TeleBot(TOKEN)

ASK = [
    'Ксюша в пути',
    'Уже выехали',
    'Готов жопу',
    'Можешь расслабить булки',
    'Катя наблюдает за тобой',
    'Берегись красного форда',
    'Кому ты сдался?',
    'Нгуен лучший',
]

ASKER = [
    'Почему повышаются цены на сигареты?',
    'Какие сигареты вредны?',
    'Какие соусы Вы добавляете?',
    'Что такое американская мешка табака?',
    'Какие качества каждого из табаков?',
    'Преимущества угольного фильтра? Зачем уголь в нем?',
    'На сколько разные технологии (LSS/ Smell less) уменьшает запах дыма? ',
    'Табак выращивается в Украине?',
    'А эти табаки точно из других стран привозят или где-то в подвале выращивают?',
    'Как я могу отличить настоящую пачку от поддельной?',
    'А почему от этих  сигарет у меня першит горло, я кашляю...? ',
    'А разве вас не запретили законом?',
    'Если конкуренты нарушают закон почему вы этого не делаете?',
    'Зачем вы легкие на пачке нарисовали?',
    'Выдаете ли вы на пробу сигареты?',
    'А зачем мне ваша информация?',
    'А Вы были на фабрике и видели лично из чего сигареты делают?',
    'Какая бумага используется в сигаретах? Что входит в состав сигаретной бумаги?',
    'Если оторвать фильтр то сигареты станут крепче? ',
    'Ваши сигареты стали плохими и я не хочу их курить.',
    'Какие сигареты производит компания Marvel International Tobacco Group?',
    'Где производятся сигареты ТМ ___? ',
    'Что означает буква "М"?',
    'Проверяют ли табак на радиоактивность?',
    'Могу ли я увидеть сертификаты качества сигарет, о которых вы мне рассказали?',
    'Импортные сигареты лучше, чем те, что производятся в Украине?',
    'А почему Вы не указываете информацию о сортах табака на пачке, для того, чтобы я мог ее прочитать?',
    'В чем основное отличие сигарет от сигарилл?',
    'Вопрос о ароматизаторах, какие мы используем и какой эффект они дают?',
    'Можно купить Сигареты /сигариллы по штучно? И почему ?',
    'Кто владелец компании Marvel-ITG?',
]


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, """
    Привет!
Меня зовут Мурлен и я стремлюсь сделать каждого консултанта счастливым!
/sv - Просмотр местонахождения СВ
/askme - Случайный вопрос
/doc - Получить документацию
/help - Описание бота
Напиши "Ко мне приедут св?" чтобы узнать к чему готовиться)))
    """)
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['askme'])
def command_handler(message: Message):
    bot.reply_to(message, random.choice(ASKER))
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['sv'])
def command_handler(message: Message):
    bot.reply_to(message, """
 Для того, чтобы узнать последние местоположение СВ тыкни на хэштег снизу:
     #СВ
        """)
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['doc'])
def command_handler(message: Message):
    bot.reply_to(message, """
 Для того, чтобы получить всю документацию перейдите по ссылке ниже:
     https://t.me/joinchat/AAAAAEnJZ5hWhs1SyJDlZA
        """)
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_message(message: Message):
    if 'Я ебу собак' in message.text:
        bot.reply_to(message, 'Всегда готов\nТрахнуть сразу несколько котов)')
        return
    if 'Привет' in message.text:
        bot.reply_to(message, 'Приветствую тебя, консультант!)')
        return
    if 'Дима' in message.text:
        bot.reply_to(message, 'Побережец Дмитрий Александрович является ненатуралом)')
        return
    if 'Где св' in message.text:
        bot.reply_to(message, """
         Для того, чтобы узнать последние местоположение СВ тыкни на хэштег снизу:
             #СВ
                """)
        return
    if 'Цыган' in message.text:
        bot.reply_to(message, 'Аширов и Нгуен - самые лучшие!')
        return
    if 'цыган' in message.text:
        bot.reply_to(message, 'Не пизди на цыган, если нет лишнего коня!')
        return
    if 'Ко мне приедут св?' in message.text:
        bot.reply_to(message, random.choice(ASK))
        return
    if 'Доброе утро' in message.text:
        bot.reply_to(message, 'Утро добрым не бывает, когда тебе на смену скоро :D')
        return


bot.polling(none_stop=True)
