import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = '7583145649:AAFHwBXLVNs7AMFq3r59gMTAm45ANUtfpf0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.new_chat_members)
async def new_member_handler(message: Message):
    await message.delete()

@dp.message(F.left_chat_member)
async def left_member_handler(message: Message):
    await message.delete()

@dp.message(F.text == "/start", F.chat.type == "private")
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "Men KirChiq Bot 🤖\n"
        "Guruhingizdagi kirgan yoki chiqqan a’zolarning xabarlarini jim o‘chiraman 🧼\n\n"
        "🛠 Faqat meni guruhga admin qiling – bo‘ldi 😎"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
