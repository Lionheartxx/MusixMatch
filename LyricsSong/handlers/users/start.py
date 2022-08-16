import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 {message.from_user.full_name}\n\n"
                         f"Этот бот ищет тексты песен по их названиям. Чтобы выполнить поиск, отправьте мне название песни!")
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name, username=f"@{message.from_user.username}", language=f"<b>{message.from_user.language_code.upper()}</b>")
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"<b>{message.from_user.full_name}</b>\n" \
              f"<b>@{message.from_user.username}</b>\n" \
              f"<b>ID: {message.from_user.id}</b>\n" \
              f"<b>{message.from_user.language_code.upper()}</b>\n" \
              f"______________________________\n" \
              f"Bazaga qo'shildi\n" \
              f"Bazada <b>{count}</b> ta foydalanuvchi bor"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except sqlite3.IntegrityError:
        again = f"<b>{message.from_user.full_name}</b>\n" \
                f"<b>@{message.from_user.username}</b>\n" \
                f"<b>ID: {message.from_user.id}</b>\n\n"
        await bot.send_message(chat_id=ADMINS[0], text=f"{again}🔄 foydalanuvchi qayta start bosdi")
