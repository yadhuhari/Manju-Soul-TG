from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random

PICS = [
 "https://telegra.ph/file/47ee5f28d4e1fd92b2e69.jpg",
 "https://telegra.ph/file/a6fd611ade419c48e1f27.jpg",
 "https://telegra.ph/file/930b866a102409f3ae4be.jpg"
]




@SOULTG.on_message(filters.private("Hridayam"))
async def Hridayam(client, message):
  await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
🔅TITLE    : HRIDAYAM
🔅YEAR     : 2022
🔅FILES    : 3
🔅UPLOADED : @MANJUTGBOT

   ⭕DOWNLOAD NOW⭕
    t.me/SoulBotzz
    t.me/SoulBotzz
    t.me/SoulBotzz
    t.me/SoulBotzz
    
@SoulBotzz
"""
)
