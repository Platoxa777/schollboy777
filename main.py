from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio

# Инициализация бота и диспетчера
bot = Bot(token='7531766827:AAGwvfLvcXl90cd3QNtTmqlBIvuHsmwNZq4')
dp = Dispatcher()


# Обработчик команды /start и /help
@dp.message(Command(commands=['start', 'help']))
async def start(message: types.Message):
    # Создаем кнопку с веб-приложением
    button = KeyboardButton(text='Открыть игру', web_app=WebAppInfo(url='https://github.com/Platoxa777/schollboy.git/telegram.html'))

    # Создаем клавиатуру и передаем в нее список кнопок
    markup = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)

    # Отправляем приветственное сообщение с клавиатурой
    await message.answer('Привет, мой друг! Готов начать игру?', reply_markup=markup)


# Функция для запуска бота
async def main():
    # Начинаем polling (опрос)
    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())

