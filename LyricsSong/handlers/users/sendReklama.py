import asyncio
from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from states.personalReklama import PersonalData
from data.config import ADMINS


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def get_reklama(message: types.Message):
    await message.answer("Reklamani yuboring 📜")
    await PersonalData.adminsReklama.set()


@dp.message_handler(state=PersonalData.adminsReklama, content_types=types.ContentTypes.ANY)
async def send_reklama(message: types.Message, state: FSMContext):
    if message.text == "/stopreklama":
        await state.finish()
        await message.answer("Reklama bekor qilindi ✖")
    else:
        users = db.select_all_users()
        for user in users:
            user_id = user[0]
            await bot.copy_message(chat_id=user_id, from_chat_id=message.chat.id, message_id=message.message_id)
            await asyncio.sleep(0.05)
        await state.finish()
    await state.finish()