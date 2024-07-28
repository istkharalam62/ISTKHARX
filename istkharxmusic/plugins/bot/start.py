import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.future import VideosSearch

import config
from istkharxmusic import app
from istkharxmusic.misc import _boot_
from istkharxmusic.plugins.sudo.sudoers import sudoers_list
from istkharxmusic.utils.database import get_served_chats, get_served_users, get_sudoers
from istkharxmusic.utils import bot_sys_stats
from istkharxmusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from istkharxmusic.utils.decorators.language import LanguageStart
from istkharxmusic.utils.formatters import get_readable_time
from istkharxmusic.utils.inline import first_page, private_panel, start_panel
from config import BANNED_USERS, AMOP
from strings import get_string



YUMI_PICS = [
"https://telegra.ph/file/2e85d11aefdf6cd01301b.jpg",
"https://telegra.ph/file/0a08b180583f13952336a.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/bb0a28259990c6a978985.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/a0db46dfacd94e489117b.jpg",
"https://telegra.ph/file/cd77be2595cdc2fca60a3.jpg",
"https://telegra.ph/file/632724b3d30c691247c77.jpg",
"https://telegra.ph/file/a2d01afe4f2cb1d4b650c.jpg",
"https://telegra.ph/file/94dc035df11dfb159b999.jpg",
"https://telegra.ph/file/fed9a5b1cbaaefc3a818c.jpg",
"https://telegra.ph/file/66fd03632cbb38bdb4193.jpg"

]



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(YUMI_PICS),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
