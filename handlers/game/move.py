import logging
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp, bot
from keyboards.inline.buttons import keyboard_move

btn_res = {1: 49,
           2: 50,
           3: 51,
           4: 52,
           5: 53,
           6: 54,
           7: 55,
           8: 56,
           9: 57
           }


@dp.message_handler(commands=['test'])
async def send_board(message: types.Message):
    await message.answer(text=
 f"""
 -----------------
 - {chr(btn_res.get(1))} - {chr(btn_res.get(2))} - {chr(btn_res.get(3))} -
 -----------------
 - {chr(btn_res.get(4))} - {chr(btn_res.get(5))} - {chr(btn_res.get(6))} -
 -----------------
 - {chr(btn_res.get(7))} - {chr(btn_res.get(8))} - {chr(btn_res.get(9))} -
 -----------------
 """,
                         reply_markup=keyboard_move)


@dp.callback_query_handler(text_contains="1")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 1")
    btn_res[1] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="2")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 2")
    btn_res[2] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="3")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 3")
    btn_res[3] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="4")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 4")
    btn_res[4] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="5")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 5")
    btn_res[5] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="6")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 6")
    btn_res[6] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="7")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 7")
    btn_res[7] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="8")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 8")
    btn_res[8] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="9")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы походили на поле 9")
    btn_res[9] = 10060
    await send_board(call.message)


@dp.callback_query_handler(text_contains="loss")
async def move_one(call: CallbackQuery):
    await call.answer(cache_time=60)
    logging.info(f"call = {call.data}")
    await call.message.answer(f"Вы сдались")

# @dp.message_handler(commands=['test_menu'])
# async def send_welcome(message: types.Message):
#     await message.reply("Test menu ", reply_markup=menu_2)


