import re
from pyrogram import filters
import random
from AarohiX import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ɴɪɢʜᴛ ❀.\n\n✦ ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐐ᴜᴇᴇɴ ✘ 𝐌ᴜꜱɪᴄ 🌙**")
    else:
    
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**❀ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ɴɪɢʜᴛ ❀.\n\n✦ ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\n✦ ᴡɪsʜɪɴɢ ᴛᴏ ➛ {sender}!\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 𝐐ᴜᴇᴇɴ ✘ 𝐌ᴜꜱɪᴄ {emoji}**")


