import re
import numpy as np
from requests.exceptions import HTTPError, Timeout
import lyricsgenius
########################################################################
def jsonExtract(obj, key):
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
########################################################################

# CLIENT_ID = "obkEMOCpvvOZPl3TZHqQINo88GAf_nHdPK4vLkk2J2Bb5khsOODmdATA1sJmYt08"
# CLIENT_SECRET = "LUpZc94sSZEAmUofoseUTO7UCX9ciYTy95wIxA6dEiNKILia1Tu6-eKFEYw5QiEHaZKVEigbYdCYneDtFpah9w"
CLIENT_ACCESS_TOKEN = "ZdVQ6oSWa8c9d93eF0TW83gHg2vHIEUXXx3DZD4vsUad1g8UQFniuxRtAjypdoPw"

genius = lyricsgenius.Genius(CLIENT_ACCESS_TOKEN)
genius.timeout = 5
genius.sleep_time = 0.2

from keyboards.inline.SelectButton import SelectSong
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp

########################################################################
numbered_songs = []

@dp.message_handler()
async def Send_List(message: types.Message):
    def ListOfSongs(search_songs):
        try:
            song = genius.search_songs(f"{search_songs}")

            list_of_artist = []
            list_of_song = []
            for artist_name in jsonExtract(song['hits'], 'artist_names'):
                list_of_artist.append(artist_name)

            for song_name in jsonExtract(song['hits'], 'title'):
                list_of_song.append(f"{song_name}")

            arr = np.dstack((list_of_artist, list_of_song))
            len_arr = len(arr[0])

            for res in arr[0][range(0, len_arr)]:
                numbered_songs.append(f"{res[0]} - {res[1]}")
                # print(f"{res[0]} - {res[1]}")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass

    if len(numbered_songs) == 0:
        ListOfSongs(search_songs=message.text)
    else:
        numbered_songs.clear()
        ListOfSongs(search_songs=message.text)

    if len(numbered_songs) == 10:
        await message.answer(f"Результаты 1-10\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n"
                             f"6.  {numbered_songs[5]}\n"
                             f"7.  {numbered_songs[6]}\n"
                             f"8.  {numbered_songs[7]}\n"
                             f"9.  {numbered_songs[8]}\n"
                             f"10.  {numbered_songs[9]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 9:
        await message.answer(f"Результаты 1-9\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n"
                             f"6.  {numbered_songs[5]}\n"
                             f"7.  {numbered_songs[6]}\n"
                             f"8.  {numbered_songs[7]}\n"
                             f"9.  {numbered_songs[8]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 8:
        await message.answer(f"Результаты 1-8\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n"
                             f"6.  {numbered_songs[5]}\n"
                             f"7.  {numbered_songs[6]}\n"
                             f"8.  {numbered_songs[7]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 7:
        await message.answer(f"Результаты 1-7\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n"
                             f"6.  {numbered_songs[5]}\n"
                             f"7.  {numbered_songs[6]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 6:
        await message.answer(f"Результаты 1-6\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n"
                             f"6.  {numbered_songs[5]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 5:
        await message.answer(f"Результаты 1-5\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n"
                             f"5.  {numbered_songs[4]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 4:
        await message.answer(f"Результаты 1-4\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n"
                             f"4.  {numbered_songs[3]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 3:
        await message.answer(f"Результаты 1-3\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n"
                             f"3.  {numbered_songs[2]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 2:
        await message.answer(f"Результаты 1-2\n\n"
                             f"1.  {numbered_songs[0]}\n"
                             f"2.  {numbered_songs[1]}\n", reply_markup=SelectSong)
    elif len(numbered_songs) == 1:
        await message.answer(f"Результаты 1-1\n\n"
                             f"1.  {numbered_songs[0]}\n", reply_markup=SelectSong)
    else:
        await message.answer("Такой песен не найдено 🤔")

########################################################################
@dp.callback_query_handler(text="1")
async def Send_Lyric(call: CallbackQuery):
    if 1 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[0]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="2")
async def Send_Lyric(call: CallbackQuery):
    if 2 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[1]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="3")
async def Send_Lyric(call: CallbackQuery):
    if 3 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[2]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="4")
async def Send_Lyric(call: CallbackQuery):
    if 4 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[3]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="5")
async def Send_Lyric(call: CallbackQuery):
    if 5 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[4]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="6")
async def Send_Lyric(call: CallbackQuery):
    if 6 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[5]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="7")
async def Send_Lyric(call: CallbackQuery):
    if 7 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[6]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="8")
async def Send_Lyric(call: CallbackQuery):
    if 8 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[7]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="9")
async def Send_Lyric(call: CallbackQuery):
    if 9 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[8]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################
@dp.callback_query_handler(text="10")
async def Send_Lyric(call: CallbackQuery):
    if 10 <= len(numbered_songs):
        await call.message.delete()
        await call.message.answer("🔎 Ищу тексты песен...")
    else:
        await call.message.answer(f"Список ограничен {len(numbered_songs)} строками ☝🤓")
    full_text = []
    def GetText():
        song_name = numbered_songs[9]

        artist_get = song_name.split("-")
        artist_name = artist_get[0].strip()
        r = re.sub(r'\([^)]*\)', '', artist_name)

        song_get = song_name.split("-")
        song_get_name = song_get[1].strip()

        try:
            artist = genius.search_artist(r, max_songs=1)
            song_text = artist.song(song_get_name)
            text = song_text.lyrics
            full_text.append(f"<code>{artist_name} - {song_get_name}</code>\n\n"
                             f"{text[:-5]}\n\n"
                             f"<i>через @MusixMBot</i>")
        except HTTPError as e:
            print(e.errno)
            print(e.args[0])
            print(e.args[1])
        except Timeout:
            pass
    GetText()
    try:
        await call.message.answer(full_text[0])
    except:
        await call.message.answer("Повторите попытку 🫥")
    full_text.clear()
########################################################################