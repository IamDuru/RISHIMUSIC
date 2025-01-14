from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from RISHUMUSIC import app
from RISHUMUSIC.utils.database import add_served_chat_clone, delete_served_chat_clone
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RISHUMUSIC.utils.database import get_assistant
import asyncio
from RISHUMUSIC.misc import SUDOERS
from RISHUMUSIC.mongo.afkdb import LOGGERS as OWNERS
from RISHUMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from RISHUMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from RISHUMUSIC import app
from RISHUMUSIC.utils.shukla_ban import admin_filter
from RISHUMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from RISHUMUSIC.utils.database import get_assistant, is_active_chat


@Client.on_message(filters.command("re63636pbbo") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1845472a641e97ac614a4.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com")
                 ]
            ]
        ),
    )

@Client.on_message(filters.command("rbb636epo") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1845472a641e97ac614a4.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                 ]
            ]
        ),
    )

@Client.on_message(filters.command("re276bbbpo") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1845472a641e97ac614a4.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/")
                 ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@Client.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat_clone(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio
import time


@Client.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @vip_music_vc_bot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await client.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001992970818:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")