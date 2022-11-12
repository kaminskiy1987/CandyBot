# юда все функции отправляющие сообщения


from aiogram import types

from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки'
                           f'Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\
                            Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
                            Все конфеты оппонента достаются сделавшему последний ход.')

#async def start_game(update):
#    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
#       Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\
#       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
#       Все конфеты оппонента достаются сделавшему последний ход.')


async def table_info(message: types.Message(), name: str, count: int, total_count: int, name2: str):
    await bot.send_message(message,
                           f'{name} взял {count} конфет\nИ на столе осталось {total_count} конфет\nХод {name2}')


async def wrong_take(message: types.Update()):
    await bot.send_message(message,
                           f'Ты взял конфет больше чем нужно (или меньше)! Попробуй еще раз')


async def player_take(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Возьмите конфеты, но не больше 28: ')


async def win(message: types.Message, name:str):
    await bot.send_message(message,
                           f'{name} выиграл!')