from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
import sys, re
from aiogram import F
from aiogram.types import InlineKeyboardMarkup,  InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from random import randrange
from dotenv import load_dotenv
import os


load_dotenv()




TOKEN = os.getenv('TOKEN')


dp = Dispatcher()

bot = Bot(token = TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))




def reply_buttons():

    kbs = [
     [types.KeyboardButton(text='/start')],[types.KeyboardButton(text='/help')],
     [types.KeyboardButton(text='/location', request_location = True)],[types.KeyboardButton(text='/telefon',request_contact= True)],
     [types.KeyboardButton(text='/hisoblash')
      ]
        ]
    
    keyboard =types.ReplyKeyboardMarkup(keyboard= kbs, resize_keyboard=True)
    return keyboard



@dp.message(Command('start'))
async def start_button(message: Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.first_name},Sizning ID: {message.from_user.id}",reply_markup = reply_buttons())






#footer
async def main() -> None:
  
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
