#!/usr/bin/python
# -*- coding: utf-8 -*-
import config, logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from datetime import datetime, timedelta

bot = Bot(token=config.token, parse_mode="html")
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)

dp.filters_factory.bind(IsChannelFilter)

@dp.message_handler(commands="start")
async def start(message):
    await bot.send_message(f"<b>😁Я бот анти канал чатов!\n Я запрещаю людям писать от имени канала в чатах\n\nНаписал бота > @NoZiss для канала портфолио</b>")

class IsChannelFilter(BoundFilter):
    key = "is_channel"
    
    def __init__(self, is_channel):
        self.is_channel = is_channel

@dp.message_handler(is_channel=True)
async def handler_anti_channel(message: types.Message):
    await bot.ban_chat_sender_chat(message.chat.id, message.sender_chat.id)
    await bot.send_message(message.chat.id, f"<b>😁 Канал был добавлен в чёрный список, и вы не можете с него писать в этот чат</b>")
   
if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=False)
