from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import TOKEN

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, storage=storage)
