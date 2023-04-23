import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين ستار","المطورين","السورس مطورين","مطورين star"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/abc6b25ceb81316ab1e1e.jpg",
        caption=f"""**──── 「 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 」────**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين star ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**──── 「 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 」────**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒- 𝙎 𝙄 𝙈 𝙊 -", url=f"https://t.me/DaRrKNneSs_1"), 
                 ],[
                    InlineKeyboardButton(
                        "- 𝙍 𝙊 𝙒 𝙀 𝙎 -", url=f"https://t.me/RQ_X0"),
                ],[
                    InlineKeyboardButton(
                        "「 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 」", url=f"https://t.me/S0URCE_STAR"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["رويس","رويس الهقر","الهقر","ROWES","rowes","RoWeS","Rowes"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("RQ_X0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**──── 「 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 」────\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**──── 「 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙏𝘼𝙍 」────**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
