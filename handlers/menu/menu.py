import logging

from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.buttons import keyboard_menu, keyboard_create_game, keyboard_join_game_back
from loader import dp

from keyboards.reply_keyboard.buttons import menu_1
from states import GameState


@dp.message_handler(text='Меню')
@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.answer("Меню", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Что вы хотете сделать?", reply_markup=keyboard_menu)


@dp.callback_query_handler(text="menu:create_game")
async def send_create_game(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.edit_text(
        f"Вы хотите создать игру\nКакую игру выхоитети создать? Открытую для всех или закрутыую",
        reply_markup=keyboard_create_game)


@dp.callback_query_handler(text="menu:find_game")
async def send_find_game(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.edit_text(f"Вы хотите найти игру", reply_markup=keyboard_menu)



@dp.callback_query_handler(text="menu:join_game")
async def send_join_game(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.edit_text(f"Вы хотите присоеденится к игре\nВведите код игры",
                                 reply_markup=keyboard_join_game_back)
    await GameState.game_code.set()

