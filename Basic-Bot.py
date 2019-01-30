''' Got base code from this tutorial: https://www.devdungeon.com/content/make-discord-bot-python'''
# Written in Python 3.6
import discord

TOKEN = '# Bot Token'

client = discord.Client()

@client.event
async def on_message(message):
    # Prevents the bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!goodbye'):
        msg = 'Nice knowing ya!'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('hello'):
        await client.send_message(message.channel, "World")

    # At the moment this will only work with whoever you specify to be mentioned
    if message.content.startswith('!Say hello to #user'):
        await client.send_message(message.channel, 'Hello, <@!# User ID>!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Making a bot"))

client.run(TOKEN)
