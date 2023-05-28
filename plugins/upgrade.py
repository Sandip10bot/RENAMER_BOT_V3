"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited
	Price Rs 100  🇮🇳/🌎 2$  per Month
	
	
	Pay Using Upi I'd ```greymatter658@ybl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "@Sandip10x")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "@Sandip10x"),
        			InlineKeyboardButton("Other Methods",url = "@Sandip10x")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited 
	Price Rs 100  🇮🇳/🌎 2$  per Month
	
	
	 Admin:@Sandip10x
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "@Sandip10x")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "@Sandip10x"),
        			InlineKeyboardButton("Other Methods",url = "@Sandip10x")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
