import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import handlers
from environs import Env
import logging
env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

# Включаем логирование, чтобы не пропустить важные сообщения
# Объект бота
logging.basicConfig(level=logging.INFO)

# Запуск бота


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(handlers.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
