from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("Youtube tutorial", url="https://telegra.ph/file/27fefe183e306ef919437.jpg")],
		 ])
	help_image = "https://telegra.ph/file/a0c714ea372017109ff4c.jpg"
	await message.reply_photo(help_image,  caption="**♔English help**\n• Just Send your Youtube video url⛓ \n• And i will give Method list to select your choice😋\n\n**♔සිංහල උදව්**\n• කොපි කරගත් Youtube ලින්කුව එවන්න.\n• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය පමාණය හා මාදිලිය තෝරාදෙන්න.\n\n\n • This bot is fully free.\n• Don't pay anyone for Bots like this. \n\nAlso use our file renamer @Renamerv12bot",reply_markup=Lasiya2)
