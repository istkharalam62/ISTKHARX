import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from istkharxmusic import app


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "á´˜ÊŸá´‡á´€sá´‡ Ê€á´‡á´˜ÊŸÊ á´›á´ á´€ á´á´‡á´…Éªá´€ á´›á´ á´œá´˜ÊŸá´á´€á´… á´É´ á´›á´‡ÊŸá´‡É¢Ê€á´€á´˜Êœ"
        )
    try:
        text = await message.reply("á´˜Ê€á´á´„á´‡ssÉªÉ´É¢...")

        async def progress(current, total):
            await text.edit_text(f"ðŸ“¥ á´…á´á´¡É´ÊŸá´á´€á´…ÉªÉ´É¢... {current * 100 / total:.1f}%")

        try:
            location = f"cache"
            local_path = await message.reply_to_message.download(
                location, progress=progress
            )
            await text.edit_text("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺..")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"ðŸŒ | [LO HO GYA ISTKHAR KO PAPA BOL](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "á´›á´‡ÊŸá´‡É¢Ê€á´€á´˜Êœ ÊŸÉªÉ´á´‹",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            os.remove(local_path)
        except Exception as e:
            await text.edit_text(f"âŒ |Ò“ÉªÊŸá´‡ á´œá´˜ÊŸá´á´€á´… Ò“á´€ÉªÊŸá´‡á´… \n\n<i>Ê€á´‡á´€sá´É´: {e}</i>")
            os.remove(local_path)
            return
    except Exception:
        pass
