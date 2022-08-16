from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Введите название песни! ",
            "Пример:",
            "1. название песни - <b>You my heart</b>",
            "2. название песни и исполнитель -<b>You my heart Modern Talking</b>",)
    
    await message.answer("\n".join(text))
