from pyrogram import Client, filters
from pyrogram.types import Message
from BADMUSIC import app

# Owner's Telegram User ID
OWNER_ID = 7009601543  # Replace with your Telegram user ID

# Path to warning image (ensure the file exists)
WARNING_IMAGE_PATH = "https://files.catbox.moe/bnubd6.jpg"  # Replace with the path to your image file

# Dictionaries to track PM security and message counts for users
pm_security_status = {}
message_count = {}

# Function to check if the command is from the owner
def is_owner(user_id):
    return user_id == OWNER_ID

# Command to enable PM Security for a specific user (Owner only)
@Client.on_message(filters.private & filters.command("enablepm"))
async def enable_pm_security(client: Client, message: Message):
    if not is_owner(message.from_user.id):
        await message.reply_text("❌ Sirf owner hi is command ka use kar sakte hain.")
        return

    if len(message.command) < 2:
        await message.reply_text("❌ User ID specify karein. Example: `/enablepm 987654321`")
        return

    try:
        target_user_id = int(message.command[1])
        pm_security_status[target_user_id] = True
        message_count[target_user_id] = 0  # Reset message count when enabled
        await message.reply_text(f"✅ PM Security {target_user_id} ke liye enable kar di gayi.")
    except ValueError:
        await message.reply_text("❌ Invalid User ID format. User ID numbers mein hone chahiye.")

# Command to disable PM Security for a specific user (Owner only)
@Client.on_message(filters.private & filters.command("disablepm"))
async def disable_pm_security(client: Client, message: Message):
    if not is_owner(message.from_user.id):
        await message.reply_text("❌ Sirf owner hi is command ka use kar sakte hain.")
        return

    if len(message.command) < 2:
        await message.reply_text("❌ User ID specify karein. Example: `/disablepm 987654321`")
        return

    try:
        target_user_id = int(message.command[1])
        pm_security_status[target_user_id] = False
        await message.reply_text(f"❌ PM Security {target_user_id} ke liye disable kar di gayi.")
    except ValueError:
        await message.reply_text("❌ Invalid User ID format. User ID numbers mein hone chahiye.")

# Handle all other PMs and auto-block unauthorized users
@Client.on_message(filters.private & ~filters.service & ~filters.command(["enablepm", "disablepm"]))
async def pm_handler(client: Client, message: Message):
    user_id = message.from_user.id

    # Check if PM is enabled for the user
    if pm_security_status.get(user_id, False):  # Default to False if user not in dictionary
        await message.reply_text("✅ Aap PM kar sakte hain.")
    else:
        # Increment message count for the user
        message_count[user_id] = message_count.get(user_id, 0) + 1
        if message_count[user_id] > 3:
            await message.reply_photo(
                WARNING_IMAGE_PATH,
                caption="❌ Aapne allowed limit (3 messages) se zyada messages bheje. Aapko block kiya ja raha hai."
            )
            await client.block_user(user_id)
        else:
            remaining = 3 - message_count[user_id]
            await message.reply_photo(
                WARNING_IMAGE_PATH,
                caption=f"⚠️ Aapke paas sirf {remaining} aur messages bhejne ki permission hai. `/enablepm` ka use karein PM allow karne ke liye (Owner se request karein)."
            )
