from aiogram import types
from aiogram import Router
from aiogram.filters import CommandStart, Command

from bot.handlers.commands.command_text import *
from bot.handlers.commands.command_kb import *

from database.bot_database import bot_db

command_router = Router()


@command_router.message(Command('start'))
async def send_start(msg: types.Message):
    await msg.delete()
    await msg.answer(text=start_text)
    message = await msg.answer(text='🧾 Главное меню',
                               reply_markup=await start_kb())
    await bot_db.set_user_message(user_id=msg.from_user.id, message_id=message.message_id)
    if not await bot_db.is_user_exists(user_id=msg.from_user.id):
        await bot_db.add_user(user_id=msg.from_user.id)