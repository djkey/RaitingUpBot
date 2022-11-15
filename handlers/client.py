from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import dispatcher
from keyboards import kb_client


# class FSMorder(StatesGroup):
#     index = State()
#     count = State()

# @dispatcher.message_handler(commands='start')


async def start(message: types.Message):
    await message.answer(f'🎉🎉🎉Привет {message.from_user.first_name}🎉🎉🎉.\n🧙Я тот, кто поможет тебе прокачать🥇 твою страницу!!!\n\nБлагодаря мне ты сможешь получить лайки👍, подписчиков👯, комментарии💌 к своим постам и многое другое.☺️', reply_markup=kb_client)


# @dispatcher.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(f'{message.from_user.first_name}: {message.from_user.id}', reply_markup=ReplyKeyboardRemove())


async def history_order(message: types.Message):
    await message.answer(f'список\nID заказа:\nназвание услуги:\nзаказаное количество:\nСтатус:')


async def payment(message: types.Message):
    await message.answer('У тебя {}грн')


async def payment_history(message: types.Message):
    await message.answer('1.01.2000 пополнение на {}грн\n2.01.2000 списание на {}грн')


# async def choose_order(message: types.Message, state=FSMorder):
#     await FSMorder.index.set()
#     async with state.proxy() as data:
#         data['index'] = 0
#     await message.reply(f'Выбери что будем накручивать', reply_markup=kb_order)


# async def Roun(message: types.Message, state=FSMorder):
#     async with state.proxy() as data:
#         round = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         i = data['index']
#         await message.reply(f'{round[i]}\\10\nназвание: ...\nописание: ...\nЦена за тысячу=10$', reply_markup=kb_round)


# async def next(message: types.Message, state=FSMorder):
#     async with state.proxy() as data:
#         data['index'] += 1
#     await Roun(message=message, state=state)


# async def prev(message: types.Message, state=FSMorder):
#     async with state.proxy() as data:
#         data['index'] -= 1
#     await Roun(message=message, state=state)


# async def main_menu(message: types.Message, state=FSMorder):
#     await start(message=message)
#     await state.finish()


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start, commands='start')
    dispatcher.register_message_handler(help, commands='help')
    dispatcher.register_message_handler(history_order, lambda message: message.text == '📜История заказов')
    dispatcher.register_message_handler(payment, lambda message: message.text == '👛Посмотреть баланс')
    dispatcher.register_message_handler(payment_history, lambda message: message.text == '⚙История баланса')
    # dispatcher.register_message_handler(choose_order, lambda message: message.text == '💼Выбор заказа', state=None)
    # dispatcher.register_message_handler(Roun, lambda message: message.text in {'Лайки', 'Подписки', 'Просмотры', 'Что-то ещё'}, state='*')
    # # or 'Подписки' or 'Просмотры' or 'Что-то ещё'
    # dispatcher.register_message_handler(next, lambda message: message.text == 'Следующий', state='*')
    # dispatcher.register_message_handler(prev, lambda message: message.text == 'Предыдущий', state='*')
    # dispatcher.register_message_handler(main_menu, lambda message: message.text == 'Главное меню', state='*')
