import discord
import json
import requests
from discord.ext import commands
from conf import BOT_TOKEN as TOKEN
from conf import CMD_PRE as CMD_PREFIX
demo = commands.Bot(command_prefix=CMD_PREFIX) 

@demo.command(name='test')
async def test(clienT, arg):  # test fn
    await clienT.send(arg)  
    
@demo.command(name='start')
async def start(clienT):  
    usr = clienT.message.author  
    await clienT.send('Hey, {}!\n\nHows the day Going!?'.format(usr))  

@demo.command(name='ping') #!ping "pong"
async def ping(clienT):
    await clienT.channel.send("pong")
    
@demo.command(name='print') #!print
async def print(clienT, *cmd):
    txt = ""
    for elmnt in cmd:
                  txt = txt + " " + elmnt
    await clienT.channel.send(txt)     
    
      
@demo.command(name='img')
async def img(clienT, argu): 
    response = requests.get('https://some-random-api.ml/img/{}'.format(argu)) 
    jsoon = json.loads(response.text)  

    embed = discord.Embed(color=0x72BAB6, title='Random image with {}'.format(arg_im))  
    embed.set_image(url=jsoon['link'])  #telegraph link
    await clienT.send(embed=embed)  
    
@demo.command(name='add') # "!add 1 2 " output = 3
async def addition(clienT, a,b):
    summ = int(a)+int(b)
    await clienT.send(summ)
    
@demo.command(name='minus') # "!minus 2 1" output = 1
async def substract(clienT, a,b):
    sub = int(a)-int(b)
    await clienT.send(sub)

@demo.command(name='multi') # "!multi 1 2" output = 2
async def multiplication(clienT, a,b):
    asterisk = int(a)*int(b)
    await clienT.send(asterisk)
    
@demo.command(name='div') # "!div 2 1" output = 2
async def division(clienT, a,b):
    floor = int(a)/int(b)
    await clienT.send(floor)

demo.run(TOKEN)  # launching 😌
    

