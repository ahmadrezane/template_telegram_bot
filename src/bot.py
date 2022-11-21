import os

import emoji
import telebot
from loguru import logger
from telebot import types

from src.constant import mykeyboard
from src.utils.io import read_json, write_json


class Bot:
   def __init__(self):
      self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
      self.echo_all = self.bot.message_handler(func=lambda message : True)(self.echo_all)

   def run (self):
      logger.info('Bot is running....')
      self.bot.infinity_polling()

   def echo_all(self, message):
      self.bot.send_message(message.chat.id, message.text, reply_markup=mykeyboard.first)
      print(emoji.demojize(message.text))


if __name__ == '__main__':
   bot = Bot()
   bot.run()

