import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '扶我' in message.content and '菜' in message.content:
        print('in')
        await message.channel.send(':grey_question: ')

client.run(os.environ['TOKEN'])
