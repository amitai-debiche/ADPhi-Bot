import discord
from discord.ext import commands

import os
import json
import requests
class Songs(commands.Cog):

    def __init__(self, client):
        self.client = client


    #Commands
    @commands.command()
    async def song(self, ctx, s_num=0):
        with open('/home/ami/src/venv/ADPhi-Bot/cogs/songs.json') as f:
            data = json.load(f)['songs']

        await ctx.send(data[s_num]['name'])
        await ctx.send(data[s_num]['lyrics'])
        
        if (s_num > 0 and  s_num < 11):
            name = f"./cogs/mp3files/{data[s_num]['name']}.mp3"
            await ctx.send(file=discord.File(name))

     


def setup(client):
    client.add_cog(Songs(client))

