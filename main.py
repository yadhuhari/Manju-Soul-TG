from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
from pyrogram.errors import UserNotParticipant


force_channel = "SoulBozz"


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


SOULTG = Client(
    name="Manju",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

PICS = [
 "https://telegra.ph/file/47ee5f28d4e1fd92b2e69.jpg",
 "https://telegra.ph/file/a6fd611ade419c48e1f27.jpg",
 "https://telegra.ph/file/930b866a102409f3ae4be.jpg"
]


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
        caption="""
HELLO !
MY NAME IS MANJU 💖 ,
I CAN PROVIDE MALAYALAM MOVIES FOR YOU 😎
JUST SEARCH THE MOVIE BY ITS NAME HERE AND ENJOY 😍
ARE YOU ANY DOUBT HIT HERE 👉🏻 /help 🛠

@SoulBotzz"""
      reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("UPDATE CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )

print("I AM OK DEAR 😘")

SOULTG.run()
