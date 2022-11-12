# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    #dp.register_message_handler(commands.finish, commands=['finish'])
    # dp.register_message_handler(commands.set_count, commands=['set_count'])
    #
    #dp.register_message_handler(commands.getNumber)
    #dp.register_message_handler(commands.start_game, commands=['star']))
    dp.register_message_handler(commands.player_turn)
    dp.register_message_handler(commands.bot_turn)
    dp.register_message_handler(commands.finish, commands=['finish'])