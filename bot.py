import telebot
import cfg
bot = telebot.TeleBot(cfg.TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Как дела', 'Скинь песню')
chat_id = 'https://t.me/SvRT_group'




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой Создатель', reply_markup=keyboard1)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, Создатель',reply_markup=keyboard1)
    elif message.text.lower()== 'как дела':
        bot.send_message(message.chat.id, 'Отлично, в отличии от тебя нисшее создание',reply_markup=keyboard1)
    elif message.text.lower() == 'скинь песню':
        voice =  open ('Music/POWERWOLF - Demons Are A Girls Best Friend (Cover by Radio Tapok  на русском).mp3', 'rb')
        bot.send_audio(message.chat.id, voice, reply_markup=keyboard1)
        file_id = 'pwrt'
        bot.send_document(message.chat.id, file_id)






if __name__ == '__main__':
    bot.polling(none_stop=True)