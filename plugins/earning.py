"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('earning'))
async def upgrade(bot,update):
	text = """<b>❉ Hᴏᴡ Tᴏ Eᴀʀɴ Fʀᴏᴍ Tʜɪs Bᴏᴛ</b>

<b>➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.</b>

<b>⌾ sᴛᴇᴘ 1 : ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇᴅɢᴇ.</b>

<b>⌾ sᴛᴇᴘ 𝟸 : ʏᴏᴜ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ ᴀɴʏ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ.</b>

<b>⌾ sᴛᴇᴘ 𝟹 : ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.</b>

<b>➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ", callback_data='kingmsaa')], 
        			[InlineKeyboardButton("°• ʜᴏᴍᴇ •°", callback_data='start'),
        			InlineKeyboardButton("• ᴄʟᴏꜱᴇ •", callback_data='close_data')  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["earning"]))
async def upgradecm(bot,message):
	text = """<b>❉ Hᴏᴡ Tᴏ Eᴀʀɴ Fʀᴏᴍ Tʜɪs Bᴏᴛ</b>

<b>➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.</b>

<b>⌾ sᴛᴇᴘ 1 : ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇᴅɢᴇ.</b>

<b>⌾ sᴛᴇᴘ 𝟸 : ʏᴏᴜ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ ᴀɴʏ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ.</b>

<b>⌾ sᴛᴇᴘ 𝟹 : ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.</b>

<b>➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ꜱᴇᴛ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ", callback_data='kingmsaa')], 
        			[InlineKeyboardButton("°• ʜᴏᴍᴇ •°", callback_data='start'),
        			InlineKeyboardButton("• ᴄʟᴏꜱᴇ •", callback_data='close_data')  ]])
	await message.reply_text(text = text,reply_markup = keybord)
