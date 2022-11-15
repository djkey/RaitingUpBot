from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from settings import REFERAL

status = KeyboardButton('Статус(для бота)')
payments = KeyboardButton('База платежей')
order = KeyboardButton('База заказов')
view_order = KeyboardButton('Виды заказов')
ref = KeyboardButton(f'{REFERAL}% реферала')


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.row(status, payments).row(order, view_order).row(ref)
