from handlers import client, create_order, admin, other
from aiogram.utils import executor
from create_bot import dispatcher


async def on_startup(_):
    print('бот вышел в онлайн')

client.register_handlers_client(dispatcher)
create_order.register_handlers_create_order(dispatcher)
admin.register_handlers_admin(dispatcher)
other.register_handlers_other(dispatcher)


executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
