from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import dispatcher
from keyboards import kb_order, kb_whirligig
from handlers import client


class FSMorder(StatesGroup):
    index = State()
    count = State()


async def choose_order(message: types.Message, state=FSMorder):
    await FSMorder.index.set()
    async with state.proxy() as data:
        data['index'] = 0
    await message.reply(f'Выбери что будем накручивать', reply_markup=kb_order)


async def Whirligig_like(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        # Добавить базу
        Whirligigd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = data['index']
        await message.reply(f'{Whirligigd[i]}\\10\nназвание: ...\nописание: ...\nЦена за тысячу=10$', reply_markup=kb_whirligig)


async def Whirligig_subscribe(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        # Добавить базу
        Whirligigd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = data['index']
        await message.reply(f'{Whirligigd[i]}\\10\nназвание: ...\nописание: ...\nЦена за тысячу=10$', reply_markup=kb_whirligig)


async def Whirligig_views(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        # Добавить базу
        Whirligigd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = data['index']
        await message.reply(f'{Whirligigd[i]}\\10\nназвание: ...\nописание: ...\nЦена за тысячу=10$', reply_markup=kb_whirligig)


async def Whirligig_any(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        # Добавить базу
        Whirligigd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = data['index']
        await message.reply(f'{Whirligigd[i]}\\10\nназвание: ...\nописание: ...\nЦена за тысячу=10$', reply_markup=kb_whirligig)


async def next(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        data['index'] += 1
    await Whirligig_any(message=message, state=state)


async def previous(message: types.Message, state=FSMorder):
    async with state.proxy() as data:
        data['index'] -= 1
    await Whirligig_any(message=message, state=state)


async def main_menu(message: types.Message, state=FSMorder):
    await client.start(message=message)
    await state.finish()


def register_handlers_create_order(dispatcher: Dispatcher):

    dispatcher.register_message_handler(choose_order, lambda message: message.text == '💼Выбор заказа', state=None)
    dispatcher.register_message_handler(Whirligig_like, lambda message: message.text == 'Лайки', state='*')
    dispatcher.register_message_handler(Whirligig_subscribe, lambda message: message.text == 'Подписки', state='*')
    dispatcher.register_message_handler(Whirligig_views, lambda message: message.text == 'Просмотры', state='*')
    dispatcher.register_message_handler(Whirligig_any, lambda message: message.text == 'Что-то ещё', state='*')

    dispatcher.register_message_handler(next, lambda message: message.text == 'Следующий▶', state='*')
    dispatcher.register_message_handler(previous, lambda message: message.text == '◀Предыдущий', state='*')
    dispatcher.register_message_handler(main_menu, lambda message: message.text == 'Главное меню', state='*')
