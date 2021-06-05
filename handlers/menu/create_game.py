import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.menu.menu import send_menu
from keyboards.inline.buttons import keyboard_menu, keyboard_create_game_back
from loader import dp
from db import create_game, get_game_code_by_id, delete_game

from states import GameState


@dp.callback_query_handler(text="create_game:open")
async def send_create_game_open(call: CallbackQuery, state: FSMContext):
    logging.info(f"call = {call.data}")
    logging.info(f"user_id = {call.from_user.id}")
    game_id = create_game(call.from_user.id, True)
    async with state.proxy() as data:
        data['game_id'] = game_id
    logging.info(f"game_id = {game_id}")
    game_code = get_game_code_by_id(game_id)
    logging.info(f"game_code = {game_code}")
    await call.answer(cache_time=60)
    await call.message.edit_text(
        f"Создана открытая игра. Ожидайте когда кто-нибудь присо    единится.\n"
        f"Код игры - {game_code}",
        reply_markup=keyboard_create_game_back)


@dp.callback_query_handler(text="create_game:close" )
async def send_create_game_close(call: CallbackQuery,  state: FSMContext):
    game_id = create_game(call.from_user.id, False)
    async with state.proxy() as data:
        data['game_id'] = game_id
    logging.info(f"game_id = {game_id}")
    game_code = get_game_code_by_id(game_id)
    logging.info(f"game_code = {game_code}")
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.edit_text(
        f"Создана закрытая игра. Скажите код игры вашему другу чтобы он мог присоеденится\n"
        f"Код игры - {game_code}",
        reply_markup=keyboard_create_game_back)


@dp.callback_query_handler(text="create_game:back")
async def send_create_game_back(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    async with state.proxy() as data:
        id_game = data.get('game_id')

    logging.info(f"id game = {id_game}")
    delete_game(id_game)
    await call.message.edit_text(f"Игра отменена")
    await state.finish()
    await send_menu(call.message)
