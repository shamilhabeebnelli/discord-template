import discord
import json
import requests
from discord.ext import commands
from index import BOT_TOKEN as TOKEN

demo = commands.Bot(command_prefix='!','/','#') 

@demo.command()
async def test(clienT, arg):  # test fn
    await clienT.send(arg)  
    

