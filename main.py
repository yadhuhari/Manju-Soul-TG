from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
from pyrogram.errors import UserNotParticipant


force_channel = "SoulBotzz"

SOULTG = Client(
    name="Manju",
    api_id= "19383278",
    api_hash= "6e6c8100d5564c59bfd82a7a86aadb95",
    bot_token= "5807462026:AAFVCp5tc_G9o2aX2E6g5do0rH2DBBACevI"
)

PICS = [
 "https://telegra.ph/file/9befe93227525cc5de3d7.jpg",
 "https://telegra.ph/file/a04afd5b0353d65c07050.jpg",
 "https://telegra.ph/file/1a3f98bd9e7eb4ea8d4ba.jpg"
]

START_MSG = 
"""HELLO 
MY NAME IS MANJU 💖
I CAN PROVIDE MALAYALAM MOVIES FOR YOU 😎
JUST GO TO HELP SECTION AND FOLLOW INSTRUCTIONS.
ARE YOU ANY DOUBT HIT HERE 👉🏻 /help 🛠

@SoulBotzz"""

HELP_MSG =
"""HEY
THIS IS MY HELP SECTION!
HERE IS MY COMMAND...

/start  : CHECK I AM ALIVE
/help   : HOW TO USE ME
/about  : ABOUT ME
/search : TO SEARCH MOVIES

@SoulBotzz"""

ABOUT_MSG =
"""⭕NAME     : MANJU 💖
⭕CREATOR     : [SOUL BOTZZ](t.me/SoulBotzz)
⭕LIBRARY     : [PYROGRAM](https://docs.pyrogram.org/)
⭕LANGUAGE    : [PYTHON3](www.python.org/)
⭕SERVER      : [RAILWAY](https://railway.app/)
⭕SOURCE CODE : [CLICK HERE](t.me/ManjuUpdates)
"""

SEARCH_MSG =
"""
TO SEARCH A MOVIE IS A SIMPLE THING.
JUST TAP ON THE BELOW BUTTON AND ENJOY 😍
"""



@SOULTG.on_message(filters.command("start"))
async def start_cmd(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="𝙔𝙊𝙐 𝙃𝘼𝙑𝙀 𝙏𝙊 𝙎𝙐𝘽𝙎𝘾𝙍𝙄𝘽𝙀 𝙈𝙔 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("⚡️𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇⚡️", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
    

@SOULTG.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
    
@SOULTG.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ABOUT_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
    
@SOULTG.on_message(filters.command("search"))
async def search_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=SEARCH_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("SEARCH NOW 🔍", switch_inline_query_current_chat='')
            ]]
            )
        )
print("I AM OK DEAR")

SOULTG.run()
