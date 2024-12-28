from aiogram import Bot, Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""

bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands = ["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Рады вас видеть в нашем боте")

@dp.message_handler(text = ["Urban", 'Привет бот'])
async def urban_messages(message):
    print("Urban message")
    await message.answer("Сообщение получено")

@dp.message_handler(text = ['Расскажи анекдот'])
async def funny(message):
    print("Urban message")
    await message.answer("""Мадонне 55, ее парню 22.
Тине Тернер 75, ее парню 40.
Джей Ло 42, ее парню 26.
Мэрайя Кэри 44, ее мужу 32.

Всё ещё одинока? Расслабься, твой парень ещё не родился.""")


@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer(message.text.upper())
#
#
# @dp.message_handler(commands = ["start"])
# async def urban_messages(message):
#     print("Start message")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)