import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from exception import NotFoundGame
from keyboards.inline.buttons import keyboard_menu, keyboard_join_game_back
from loader import dp, bot
from states import GameState
from db import get_game_id_by_code


@dp.message_handler(state=GameState.game_code)
async def send_get_game_code(message: types.Message, state: FSMContext):
    code = message.text
    try:

        id = get_game_id_by_code(str(code))
        logging.info(f"id = {id}")
        async with state.proxy() as data:
            data['game_code'] = code
            data['game_id'] = id
        await message.reply(f"Вы присоеденилсь к игре - {id}")
    except NotFoundGame:
        await message.reply(f"Не верный код. Повторите попытку", reply_markup=keyboard_join_game_back)


@dp.callback_query_handler(text="join_game:back")
async def send_back_find(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.edit_text(f"Вход в игру отменен")
    await state.finish()

    await call.message.answer("Что вы хотите сделать?", reply_markup=keyboard_menu)
