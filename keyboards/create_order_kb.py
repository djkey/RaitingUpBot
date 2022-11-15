from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


likes = KeyboardButton('Лайки')
subsubscribers = KeyboardButton('Подписки')
views = KeyboardButton('Просмотры')
anythings = KeyboardButton('Что-то ещё')

kb_order = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_order.row(likes, subsubscribers, views, anythings)