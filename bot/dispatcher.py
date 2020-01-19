import os

import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor

from bot.keyboards import greet_kb

bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    user = msg.from_user
    data = {
        "_id": user.id,
        "name": user.full_name
    }
    response = requests.post("http://0.0.0.0:8000/api/users/signup/", json=data)
    if response.json()["success"]:
        await msg.reply("Привет, я помогаю людям меньше курить", reply_markup=greet_kb)
    else:
        await msg.reply("Вы уже зарегистрированы", reply_markup=greet_kb)


@dp.message_handler(content_types=ContentType.TEXT)
async def process_main_caption_command(msg: types.Message):
    user_id = msg.from_user.id
    response = requests.post(f"http://0.0.0.0:8000/api/counting/smoke/{user_id}")
    if response.status_code == 200:
        await msg.reply(f"Осталось {response.json()['cigarette_balance']} сигаргет на сегодня")

if __name__ == '__main__':
    executor.start_polling(dp)
