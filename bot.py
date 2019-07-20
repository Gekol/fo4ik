import telebot
import cfg

bot = telebot.TeleBot(cfg.TOKEN)
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Привет', 'Как дела', 'Скинь песню', 'Предыдущая страница')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Инструкция', 'О боте', 'Поддержать нас', 'Следующая страница')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой Создатель', reply_markup=keyboard2)
    elif message.text.lower()== 'как дела':
        bot.send_message(message.chat.id, 'Отлично, в отличии от тебя нисшее создание',reply_markup=keyboard2)
    elif message.text.lower() == 'скинь песню':
        voice =  open ('Music/POWERWOLF - Demons Are A Girls Best Friend (Cover by Radio Tapok  на русском).mp3', 'rb')
        bot.send_audio(message.chat.id, voice, reply_markup=keyboard2)
        file_id = 'pwrt'
        bot.send_document(message.chat.id, file_id)

    elif message.text.lower() == 'инструкция':
        bot.send_message(message.chat.id, 'Инструкция временно отсутствует', reply_markup=keyboard1)
    elif message.text.lower() == 'о боте':
        bot.send_message(message.chat.id, 'Это бот Вася', reply_markup=keyboard1)
    elif message.text.lower()== 'поддержать нас':
        bot.send_message(message.chat.id, 'Порекомендуйте меня друзьям. Это самая лучшая помощь', reply_markup=keyboard1)
    elif message.text.lower() == 'следующая страница':
        bot.send_message(message.chat.id, 'Выполняю',  reply_markup=keyboard2)
    elif message.text.lower() == 'предыдущая страница':
        bot.send_message(message.chat.id, 'Выполняю',  reply_markup=keyboard1)





if __name__ == '__main__':
    bot.polling(none_stop=True)