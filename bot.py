import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import pip


bot = commands.Bot("js!")
bot_id = "<@450583639638540288>"
token = ("NDUwNTgzNjM5NjM4NTQwMjg4.De1XEQ.8HiSOJkdXafjBcC6mJC64KFfUvg")
@bot.event
async def on_ready():
    print("Developed by Cyndigo#5449")


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="js!help | Meme Nation"))

         
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong!")

                                                                             
                                 
bot.run("NDUyMjkwMzU4NjY4MTY1MTMw.DfOOJA.W1M6DU5xi0g0l8fpNktuuqYaiBQ")
