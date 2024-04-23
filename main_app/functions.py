import telebot

def send_telegram_message(bot_token, chat_id, message):
    """ Отправляем сообщение в чат бота """
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
