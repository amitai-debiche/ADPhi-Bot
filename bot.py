import discord

import os
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(client)

@client.event
async def on_message(message):
    #ignore if the message sent by bot
    if message.author == client.user:
        return
    
    #TODO: change this to $ when finished testing (conflicts with current bot)
    if message.content.startswith('!'): 
        await message.channel.send('test')
        

client.run(TOKEN)
                   
