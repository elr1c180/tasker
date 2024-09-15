import asyncio
from aiogram import Dispatcher, Bot

from handlers import start, balance, directions, themes


async def main():
    bot = Bot(token='7384609530:AAFo9zXBrEVl2EbfbPE8dF12U7TuDm6WHnA')
    dp = Dispatcher()

    dp.include_routers(start.router, 
                       balance.router, 
                       directions.router,
                       themes.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())