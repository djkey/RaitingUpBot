from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types, Dispatcher
from create_bot import dispatcher
from keyboards import kb_admin


class FSMAdmin(StatesGroup):
    command = State()


# @dispatcher.message_handler(command='...', state=None)
async def admin(message: types.Message):
    await FSMAdmin.command.set()
    await message.reply('Привет, ты попал в админку', reply_markup=kb_admin)


async def _help(message: types.Message, state=FSMAdmin):
    await message.reply('Помощь из админки')


async def cancel(message: types.Message, state=FSMAdmin):
    await message.reply('OK')
    await state.finish()


async def echo(message: types.Message, state='*'):
    await message.reply('В разработке!')


def register_handlers_admin(dispatcher: Dispatcher):
    dispatcher.register_message_handler(admin, commands='admin', state=None)
    dispatcher.register_message_handler(_help, commands='help', state='*')
    dispatcher.register_message_handler(cancel, commands='del', state='*')
