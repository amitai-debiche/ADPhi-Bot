'''Cog written by Amitai. Edited by: 
    Cog is to give user access to certain blocks inside templated excel file.
    Example, if social chair need's the social budget they can grab that info
    from within discord. Excel document can be setup with new Doc, but for time 
    being, has to use template that was designed to be read by code.'''

import openpyxl
from openpyxl import load_workbook

import os
import discord
from discord.ext import commands 

class Excel(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.name = self.checkFile()
        if self.name != "":
            self.wb = load_workbook(f'./cogs/excel/{self.name}')


   ## @commands.command()
   ## async def rushBudget():



   ## @commands.command()
   ## async def pledgeBudget():


    ##@commands.command()
   ## async def socialBudget():


    
        

    @commands.command()
    async def getDoc(self, ctx):
        xlfile = self.checkFile()
        if xlfile == "":
            await ctx.send("No excel document exists, please upload excel document")
        else:
            await ctx.send(file=discord.File(f'./cogs/excel/{xlfile}'))

    @commands.command()
    async def setDoc(self, ctx):
        xlfile = self.checkFile()
        if xlfile != "":
            await ctx.send(f'The excel file {xlfile} already exists.Please remove doc before adding, or use !replaceDoc.')
            return
        if str(ctx.message.attachments) == '[]':
            return
        else: 
            filename = ctx.message.attachments[0].filename
            if filename.endswith('.xlsx'):
                await ctx.message.attachments[0].save(f'./cogs/excel/{filename}')
                await ctx.send("Document has been saved")
            else:
                await ctx.send("Can't read this file(Not .xlsx extension.")
                
    #add warning functionality and ask user if it would like a backup of the
    #or add functionality to autocreate backup that deletes after x time when
    #remove command is used
    @commands.command()
    async def removeDoc(self, ctx):
        xlfile = self.checkFile()
        if xlfile != "":
            os.remove(f'./cogs/excel/{xlfile}')
            await ctx.send("Document has been deleted")

    def checkFile(self):
        for filename in os.listdir('./cogs/excel'):
            if filename.endswith('.xlsx'):
                return filename
        return ""

async def setup(client):
    await client.add_cog(Excel(client))
