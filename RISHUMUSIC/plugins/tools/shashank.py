from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from RISHUMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://envs.sh/Amn.jpg",
        caption=f""" 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎ᴡɴᴇʀ", url=f"https://t.me/rishu1286")
                ],
                [InlineKeyboardButton(
                        "𝐎ᴡɴᴇʀ", url=f"https://t.me/ll_RADHE7_ll")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://envs.sh/Amn.jpg",
        caption=f"""𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎ᴡɴᴇR", url=f"https://t.me/rishu1286")
                ],
                [InlineKeyboardButton(
                        "𝐎ᴡɴᴇʀ", url=f"https://t.me/ll_RADHE7_ll")
            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://envs.sh/Amn.jpg",
        caption=f"""𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎ᴡɴᴇʀ", url=f"https://t.me/rishu1286")
                ],
                [InlineKeyboardButton(
                        "𝐎ᴡɴᴇʀ", url=f"https://t.me/ll_RADHE7_ll")
            ]
            ]
        ),
    )