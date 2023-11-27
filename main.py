# -*- coding: utf-8 -*-
import asyncio
import platform
from bot.main_loader import dp, tgbot
from bot.handlers.callback.callback_handler import callback_router
from bot.handlers.states.state_handler import state_router
from bot.handlers.commands.command_handler import command_router
from bot.handlers.message.echo import echo_router

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main() -> None:
    dp.include_routers(command_router)
    dp.include_routers(callback_router)
    dp.include_routers(state_router)
    # dp.include_routers(echo_router)
    await dp.start_polling(tgbot)


if __name__ == '__main__':
    asyncio.run(main())