from aiogram import types
from bot.loader import *
from aiogram.filters import CommandStart, Command

from bot.handlers.commands.command_text import *
from bot.handlers.commands.command_kb import *

from database.bot_database import bot_db


@dp.message(CommandStart)
async def send_start(msg: types.Message):
    await msg.delete()
    if not await bot_db.is_user_exists(user_id=msg.from_user.id):
        await bot_db.add_user(user_id=msg.from_user.id)
    await msg.answer(text=start_text)
    await msg.answer(text='🧾 Главное меню', reply_markup=await start_kb())