from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg",

Hello {} Nenu string session genrate bot ni {}

┏━━━━━━━━━━━━━━━━━┓
Deploy by: @santhu_music_bot
┗━━━━━━━━━━━━━━━━━┛
𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐝𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐛𝐲 @santhu_music_bot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("𝐍𝐞𝐭𝐰𝐨𝐫𝐤​", url="https://t.me/santhuvc")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏​", url="https://t.me/santhuvc")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - about bot
/help - This Message
/start - start Bot
/generate -  Generating Session
/cancel -  process
/restart - 𝐩𝐫𝐨𝐜𝐞𝐬𝐬
"""

    # About Message
    ABOUT = """
**About This Bot** 

Generate your string using pyrogram and telethon string session by @Santhustringbot

Group Support : [Gabung](https://t.me/santhuvc)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @santhu_music_bot
    """
