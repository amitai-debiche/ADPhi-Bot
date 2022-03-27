import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

#TODO: Switch back to $ when bot is finished, conflicts with current bot
client = commands.Bot(command_prefix = '!')
status = cycle(["Status 1","Status 2", "Status 3"])

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{os.path.splitext(filename)[0]}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@client.event
async def on_ready():
    change_status.start()
    print(client)

#change's bot's game status every couple hours
@task.loop(seconds=10200)
async def change_status():
    await.client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    print("There's the thing")
    client.run(TOKEN)
                   
