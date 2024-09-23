import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart  # Импортируем фильтр для команды /start
import logging
import asyncio
import config

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токена из переменной окружения или из файла конфигурации как запасной вариант
API_TOKEN = os.getenv('BOT_TOKEN', config.BOT_TOKEN)

# Проверка, есть ли токен
if not API_TOKEN:
    raise ValueError("No BOT_TOKEN provided. Please add it to your environment, .env file or config.py.")

# Настройка логирования для мониторинга
logging.basicConfig(level=logging.INFO)

# Инициализация бота с использованием токена
bot = Bot(token=API_TOKEN)

# Инициализация диспетчера для обработки сообщений
dp = Dispatcher()

# Создание роутера для управления командами
router = Router()

# Пример обработчика команды /start
@router.message(CommandStart())  # Используем фильтр CommandStart для команды /start
async def send_welcome(message: types.Message):
    await message.reply("Привет! Добро пожаловать в моего Telegram бота.")

# Регистрация роутера в диспетчере
dp.include_router(router)

# Асинхронная функция для запуска бота
async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)  # Удаление вебхука для предотвращения конфликтов
        await dp.start_polling(bot)  # Запуск опроса
    finally:
        await bot.session.close()  # Закрытие сессии бота по завершении

# Запуск асинхронного цикла для бота
if __name__ == '__main__':
    asyncio.run(main())
