import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv
from itertools import cycle

#TODO: Switch back to $ when bot is finished, conflicts with current bot
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents=intents)
status = cycle(["Status 1","Status 2", "Status 3"])



@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{os.path.splitext(filename)[0]}')
    print("load_extensions done")

@client.command()
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')


@client.event
async def on_ready():
    change_status.start()
    print(client)

#change's bot's game status every couple hours
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


async def main():
    load_dotenv()
    print("hi")
    TOKEN = os.getenv("DISCORD_TOKEN")
    async with client:
        print("hii")
        await load_extensions()
        print("hiii")
        await client.start(TOKEN)
        print("main done")

asyncio.run(main())
