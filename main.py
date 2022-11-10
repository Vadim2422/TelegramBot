from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
count = 0
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("❤️")
b2 = KeyboardButton("/photo")
b3 = KeyboardButton("/gif")
b4 = KeyboardButton("/video")
kb.add(b1).insert(b2).add(b3).insert(b4)
ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton("VK", url="https://vk.com")

ib2 = InlineKeyboardButton("Dora", url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Dora_%282020-12-22%29.jpg/800px-Dora_%282020-12-22%29.jpg")
ikb.add(ib1, ib2)
DESCRIPTION = "Мой первый py bot"
HELP_COMMAND = """
<b>/help</b> - <i>список команд</i>
/start - начать работу с ботом 
"""


def on_start_up():
    print("Bot is up")



@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(message.from_id, HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["links"])
async def help(message: types.Message):
    await message.answer("texttexttexttexttexttexttext", reply_markup=ikb)
    await message.delete()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("text", reply_markup=kb)
    #await message.delete()


@dp.message_handler(commands=["description"])
async def description(message: types.Message):
    await message.answer("Bot")
    await message.delete()


@dp.message_handler(commands=["photo"])
async def photo(message: types.Message):
    await message.delete()
    await message.answer_photo("AgACAgQAAxkDAAIB1WNsE_L_n4d0OfimbuOwNaWd94bSAAIFrzEbBXNkU8o35kSEZ-7ZAQADAgADcwADKwQ")

@dp.message_handler(commands=["video"])
async def help(message: types.Message):
    await message.delete()
    await bot.send_video(message.chat.id, "CgACAgQAAxkDAAICiGNs1fMlvzen_5zIeyG81sU-ukwMAAJ5AwACsJZkU9vFIzLrXe5VKwQ")

@dp.message_handler(commands=["gif"])
async def start(message: types.Message):
    await message.delete()
    await message.answer_video("CgACAgQAAxkDAAICemNs1WyIHGju5n00f_xFC6YEAyTiAAJJAwAC9h5lU4Sl5dVoOR3PKwQ")

@dp.message_handler(commands=["location"])
async def start(message: types.Message):
    await message.delete()
    await message.answer_location(50, 30)

@dp.message_handler()
async def dora(message: types.Message):
    if message.text == "❤️":
        await message.answer_photo("AgACAgQAAxkDAAIB0WNsEnqJlrFmluKc1d-KvFvTIRP6AAIprjEbjAFEUKN_4dr23bDCAQADAgADcwADKwQ")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_up(), skip_updates=True)
