from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Creator ❤", url="https://t.me/Cat_of_telegramx")],
        [InlineKeyboardButton(
            "Support chat 😊", url="https://t.me/Cat_Telegram_Project_Club ")],
        [InlineKeyboardButton(
            "Updates 🎛",url="https://t.me/Cat_Telegram_Projects")]
    ])
    thumbnail_url = "https://telegra.ph/file/a488092b0f602ae43bbf0.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hi<b>{message.from_user.first_name}</b>\n\n<b>Instructions for use..</b>\n• Type /help to get instructins.\n•───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
