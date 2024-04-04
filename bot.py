from aiogram import Bot, Dispatcher, types
from django.conf import settings
from aiogram.filters.command import Command
import threading
import os
import asyncio

token = os.environ.get("API_TOKEN")
bot = Bot(token="6438571775:AAGkiDR-83pqe-p3xsxXzZ5KP6I1nN4QOUU")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello! I'm your bot.")

async def main():
    await dp.start_polling(bot)

# Вызываем main асинхронно
if __name__ == "__main__":
		asyncio.run(main())