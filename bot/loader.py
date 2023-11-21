from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram import Router

from bot.config import *


storage = MemoryStorage()
bot = Bot(token=API_KEY, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)
router = Router(name=__name__)
dp.include_routers(router)


@dp.shutdown()
async def on_shutdown():
    await bot.close()
    # await dp.close()


@dp.startup()
async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)