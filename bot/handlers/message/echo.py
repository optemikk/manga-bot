from bot.loader import *
from aiogram.types import Message


@dp.message()
async def echo(msg: Message):
    message_id = msg.message_id
    message = await bot.copy_message(message_id=message_id, from_chat_id=msg.from_user.id, chat_id=msg.from_user.id)
    print(message)