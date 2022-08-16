from aiogram import types

from data.config import ADMINS
from loader import dp, db

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    allusers = db.count_users()
    print(allusers[0])
    await message.answer(f"Bazada <b>{allusers[0]}</b> foydalanuvchi bor")

@dp.message_handler(text="/listusers", user_id=ADMINS)
async def get_list_users(message: types.Message):
    listusers = db.select_all_users()
    await message.answer(listusers)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")