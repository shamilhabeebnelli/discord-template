import discord

BOT_TOKEN = '**' # your discord token here
XX = ('start', 'help', 'about') # list of words for which bot should respond


class demobot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello {message.author.mention}')

        c = 0
        for i in XX:
            if i in message.content:
                c += 1
        if c > 0: await message.channel.send(f'{message.author.mention}, never ever do that{c}')


client = demobot()
client.run(BOT_TOKEN)
