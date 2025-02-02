import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.display_handler import register_handlers
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация хендлеров
    register_handlers(dp)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
