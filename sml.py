import discord
import json
import requests
from discord.ext import commands
from index import BOT_TOKEN as TOKEN

demo = commands.Bot(command_prefix='!','/','#') 

@demo.command()
async def test(clienT, arg):  # test fn
    await clienT.send(arg)  
    
@demo.command()
async def wave(clienT):  
    usr = clienT.message.author  
    await clienT.send('Hey, {}!\n\nHows the day Going!?'.format(usr))  

@demo.command()
async def img(clienT, argu): 
    response = requests.get('https://some-random-api.ml/img/{}'.format(argu)) 
    jsoon = json.loads(response.text)  

    embed = discord.Embed(color=0x72BAB6, title='Random image with {}'.format(arg_im))  
    embed.set_image(url=jsoon['link'])  #telegraph link
    await clienT.send(embed=embed)  


demo.run(TOKEN)  # launching 😌
    

