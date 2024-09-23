import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import Router
import asyncio

# Защищённое хранение токена в коде
API_TOKEN = "7531766827:AAGUy-ZymYI48RtnVjy3aTXPjFGbvcyDc-o"

# Проверка на наличие токена
if not API_TOKEN:
    raise ValueError("Токен не задан! Проверьте переменную API_TOKEN в коде.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
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

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот был остановлен вручную.")
