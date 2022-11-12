# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view, model
from bot import bot

import random

async def start(message: types.Message):
    await view.greetings(message)
    await model.set_game()
    #await view.greetings(message)
    name = message.from_user.first_name
    await model.set_player_name(name)
    first_turn = random.randint(0,1)
    if first_turn:
        await view.player_take(message)
    else: await bot_turn(message.from_user.id)

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')

#async def start_game(message: types.Message):
#    await model.set_game()
    #await view.greetings(message)
#    name = message.from_user.first_name
#    await model.set_player_name(name)
#    first_turn = random.randint(0,1)
#    if first_turn:
#        await view.player_take(message.from_user.id)
#    else: await bot_turn(message.from_user.id)

#async def getNumber(message: types.Message):
#    number = message.text
#    if 0 < int(number) < 29:
#        print(number)
#    else:
#        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')
        
async def player_turn(message: types.Message):
   # await start_game(message.from_user.id)
    game = await model.get_game()
    if game:
        take = 0

        if message.text == '/start':
            return
        else:
            take = int(message.text)
        if (take <= 28) and (take > 0):
            await model.set_total_count(take)
        else:
            await view.wrong_take(message.from_user.id)
            return
        name = await model.get_player_name()
        total_count = await model.get_total_count()
        await view.table_info(message.from_user.id, name, take, total_count, 'Бот')
        if await model.get_total_count() > 0:
            await bot_turn(message.from_user.id)
        else:
            await view.win(message, 'Игрок')
            await model.set_game()


async def bot_turn(message: types.Message):
    take = await model.bot_take()
    await model.set_total_count(take)
    name = await model.get_player_name()
    total_count = await model.get_total_count()
    await view.table_info(message, 'Бот', take, total_count, name)
    if await model.get_total_count() <= 0:
        await view.win(message, 'Бот')
        await model.set_game()