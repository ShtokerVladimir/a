from aiogram import Bot, Dispatcher, types
from django.conf import settings
from aiogram.filters.command import Command
import threading
import asyncio

token = settings.API_TOKEN
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello! I'm your bot.")

async def main():
    await dp.start_polling(bot)

# Вызываем main асинхронно
def run_tgbot():
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(main())

bot_thread = threading.Thread(target=run_tgbot)
bot_thread.start()