from aiogram import Bot, Dispatcher, types
from django.conf import settings
from aiogram.filters.command import Command
from celery import Celery

token = settings.API_TOKEN
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello! I'm your bot.")

app = Celery('myprototype')

@app.task
def run_bot():
  dp.start_polling(bot)