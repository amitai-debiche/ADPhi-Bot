import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

#TODO: Switch back to $ when bot is finished, conflicts with current bot
client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{os.path.splitext(filename)[0]}')

@client.event
async def on_ready():
    print(client)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    print("There's the thing")
    client.run(TOKEN)
                   
