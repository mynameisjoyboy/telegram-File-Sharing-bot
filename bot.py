from pyrogram import Client, filters

api_id = 29565403  
api_hash = "3ac0c224b618e5264a19dcdf9673ec58"
bot_token = "8140736953:AAHBvyhQMbSNOmPDLgijX-Wk0DBNUI0ItTQ"

app = Client("FileShareBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.document)
async def get_file_link(client, message):
    file_link = f"https://t.me/{message.chat.username}/{message.message_id}"
    await message.reply(f"Here is your file link:\n{file_link}")

app.run()
