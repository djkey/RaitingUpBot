from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''(Подписчики) (лайки)
(Комментарии) (Просмотры)
(Мои заказы)(Баланс)'''


choise_order = KeyboardButton('💼Выбор заказа')
history_order = KeyboardButton('📜История заказов')
show_payments = KeyboardButton('👛Посмотреть баланс')
history_payments = KeyboardButton('⚙История баланса')
referals = KeyboardButton('Реферал : {}')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(choise_order, history_order).row(
    show_payments, history_payments).row(referals)
