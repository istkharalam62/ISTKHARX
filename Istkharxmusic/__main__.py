import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from istkharxmusic import LOGGER, app, userbot
from istkharxmusic.core.call import Dil
from istkharxmusic.misc import sudo
from istkharxmusic.plugins import ALL_MODULES
from istkharxmusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("istkharxmusic.plugins" + all_module)
    LOGGER("istkharxmusic.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Dil.start()
    try:
        await Dil.stream_call("https://te.legra.ph/file/39b302c93da5c457a87e3.mp4")
    except NoActiveGroupCall:
        LOGGER("istkharxmusic").error(
            "............"
        )
        exit()
    except:
        pass
    await Dil.decorators()
    LOGGER("istkharxmusic").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ɴᴏᴡ ɢɪʙ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ ᴄʜᴜᴛ ɪɴ @LOVE_FEELINGS_WILL1"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("istkharxmusic").info(".....")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
