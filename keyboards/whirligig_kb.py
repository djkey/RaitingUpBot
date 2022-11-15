from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


next_button = KeyboardButton('Следующий▶')
ok_button = KeyboardButton('ОК👌')
previous_button = KeyboardButton('◀Предыдущий')
main_button = KeyboardButton('Главное меню')

kb_whirligig = ReplyKeyboardMarkup(
    resize_keyboard=True).row(previous_button, ok_button, next_button).row(main_button)
