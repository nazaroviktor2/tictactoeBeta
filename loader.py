import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
API_TOKEN = '1706262718:AAFwmlsfo8hBXk42Fb2vlLPrGL50gc19NQo'
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO )