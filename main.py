import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


bot = Bot(token='6414411731:AAEiWh0NcqXUNrO4ZjZW1yjNe5649KfzHoU')
dp = Dispatcher()

@dp.message(Command('start'))
async def com_start(message:Message):
    print(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    text = f'Привет мой друг, {message.from_user.first_name}'
    await bot.send_message(message.from_user.id, text=text)

def on_start():
    print('Бот встал!')

def on_finish():
    print('Бот упал!')

async def start_bot():
    dp.startup.register(on_start)
    dp.shutdown.register(on_finish)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

    