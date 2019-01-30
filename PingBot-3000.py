# Work with Python 3.6
'''This bot is meant to ping whenever someone types any character on the Standard English (US) Keyboard.'''
import discord

TOKEN = '# Bot Token'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('a'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('b'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('c'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('d'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('e'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('f'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('g'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('h'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('i'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('j'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('k'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('l'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('m'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('n'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('o'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('p'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('q'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('r'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('s'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('t'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('u'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('v'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('w'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('x'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('y'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('z'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('A'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('B'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('C'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('D'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('E'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('F'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('G'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('H'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('I'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('J'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('K'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('L'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('M'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('N'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('O'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('P'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('Q'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('R'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('S'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('T'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('U'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('V'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('W'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('X'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('Y'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('Z'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('0'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('1'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('3'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('4'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('5'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('6'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('7'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('8'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('9'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('['):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(']'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('{'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('}'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('('):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(')'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('\''):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('|'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(';'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(':'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("'"):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('"'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('<'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('>'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('?'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(','):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('.'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('/'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('-'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('_'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('='):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Pinging..."))


client.run(TOKEN)
