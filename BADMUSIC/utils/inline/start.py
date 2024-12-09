from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from BADMUSIC import app

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💠 𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂 💠",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💠 𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂 💠",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿✨", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ🥀", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons


def music_start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✰ 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ ✰",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="✰ 𝗔ʙᴏᴜ𝗧✰ ", callback_data="about"),
            InlineKeyboardButton(text="✰ 𝗦ᴜᴘᴘᴏʀ𝗧 ✰", callback_data="support"),
        ],
        [InlineKeyboardButton(text="۞ ғᴇᴀᴛᴜʀᴇ ۞", callback_data="feature")],
    ]
    return buttons
