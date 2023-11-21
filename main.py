# -*- coding: utf-8 -*-
import asyncio
import platform
from bot.loader import *

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    # from bot.handlers.message import echo
    from bot.handlers import commands

    asyncio.run(main())