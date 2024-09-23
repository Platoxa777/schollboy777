import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import Router

# Токен твоего бота
API_TOKEN = '7531766827:AAFZIlc7tdN5V_HCHbNvi2TW5VJL5IbBhPw'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=API_TOKEN)

# Инициализация диспетчера и роутера
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    # Создаём кнопку для запуска Web App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить веб-приложение", web_app=WebAppInfo(url="https://platoxa777.github.io/schollboy/"))]
    ])
    await message.answer("Добро пожаловать в игру Schoolboy! Нажмите 'Запустить веб-приложение' для начала игры.", reply_markup=keyboard)

# Основная функция для запуска поллинга
async def main():
    try:
        logging.info("Запуск поллинга...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logging.info("Поллинг был отменён.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    finally:
        await bot.session.close()
        logging.info("Сессия бота завершена.")

# Запуск бота
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот был остановлен вручную.")
