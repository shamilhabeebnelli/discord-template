import discord
import json
import requests
from discord.ext import commands
from conf import BOT_TOKEN as TOKEN
from conf import CMD_PRE as CMD_PREFIX
demo = commands.Bot(command_prefix=CMD_PREFIX) 


@demo.event
async def on_ready():
    print('Build Succeed ✅')
    
@demo.event
async def on_member_join(clienT, arg):
    print("someone joined.")

@demo.event
async def on_member_remove(self, member):
    print("someone left server.")
    
@demo.event
async def on_message(self, message):
    print(f"{message.author} just sent a message: {message.content}.")
    
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
    txt = requests.get('https://some-random-api.ml/img/{}'.format(argu)) 
    jsoon = json.loads(txt.text)  

    embed = discord.Embed(color=0x72BAB6, title='Random image with {}'.format(argu))  
    embed.set_image(url=jsoon['link'])  #telegraph link
    await clienT.send(embed=embed)  
    
@demo.command(name='add') # "!add 1 2 " output = 3
async def add(clienT, a,b):
    summ = int(a)+int(b)
    await clienT.send(summ)
    
@demo.command(name='minus') # "!minus 2 1" output = 1
async def minus(clienT, a,b):
    sub = int(a)-int(b)
    await clienT.send(sub)

@demo.command(name='multi') # "!multi 1 2" output = 2
async def multi(clienT, a,b):
    asterisk = int(a)*int(b)
    await clienT.send(asterisk)
    
@demo.command(name='div') # "!div 2 1" output = 2
async def div(clienT, a,b):
    floor = int(a)/int(b)
    await clienT.send(floor)

demo.run(TOKEN)  # launching 😌
    

