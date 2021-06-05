from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_start = KeyboardButton(text="Меню")

menu_1 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_1.row(btn_start)



