from aiogram import Bot, Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""

bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands = ["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message):
    print("Введите команду /start, чтобы начать общение.")




# @dp.message_handler(text = ["Urban", 'Привет бот'])
# async def urban_messages(message):
#     print("Urban message")
#
#
# @dp.message_handler(commands = ["start"])
# async def urban_messages(message):
#     print("Start message")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)