from aiogram import types, Dispatcher
from create_bot import dispatcher


# @dispatcher.message_handler()
async def echo_send(message: types.Message):
    await message.answer(f'other : {message.from_user.first_name}: {message.text}')


def register_handlers_other(dispatcher: Dispatcher):
    dispatcher.register_message_handler(echo_send)
