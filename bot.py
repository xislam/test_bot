from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Привет!\n Ребята пишите мне что-то и я вам это отправлю!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    if msg.text == 'Как дела?':
        await bot.send_message(msg.from_user.id, 'Хорошо ребята!!😊')




if __name__ == '__main__':
    executor.start_polling(dp)