import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
import logging
import asyncio

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токена из переменной окружения
API_TOKEN = os.getenv('7531766827:AAExZRKapjL3FMtxrOzoqRWkXM4mkeCdBDk')

# Проверка, есть ли токен
if API_TOKEN is None or API_TOKEN == '':
    raise ValueError("No BOT_TOKEN provided. Please add it to your environment or .env file.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=API_TOKEN)

# Инициализация диспетчера
dp = Dispatcher()

# Создание роутера
router = Router()

# Пример обработчика сообщений
@router.message(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Добро пожаловать в моего Telegram бота.")

# Регистрация роутера в диспетчере
dp.include_router(router)

# Асинхронная функция для запуска бота
async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
