import discord
from forex_python.converter import CurrencyRates
client = discord.Client()
#USD to TRY currency converter function
def dolar():
    c = CurrencyRates()
    return c.get_rate("USD","TRY")
#When client logged in give print for information
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
#when user use prefix that '$' do some functions according the conditions
@client.event
async def on_message(message):
    if message.content.startswith('$dolar'):
        await message.channel.send(dolar())
    if message.content.startswith('$CS'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Computer Society"))
        print(message.author)
    if message.content.startswith('$EA'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Educational Activities"))
        print(message.author)
    if message.content.startswith('$PES'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Power and Energy Society"))
        print(message.author)
    if message.content.startswith('$EdSoc'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Education Society"))
        print(message.author)
    if message.content.startswith('$ENET'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Entrepreneurship"))
        print(message.author)
    if message.content.startswith('$RAS'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Robotics & Automation"))
        print(message.author)
    if message.content.startswith('$AESS'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Aeorospace and Electronic System Society"))
        print(message.author)
    if message.content.startswith('$WIE'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Women in Engineering"))
        print(message.author)
    if message.content.startswith('$EMBS'):
        await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Engineering in Medicine and Biology Society"))
        print(message.author)
    if message.content.startswith('$IEEE'):
        await message.channel.send("https://www.instagram.com/ieeeegesb/")
        print(message.author)
#run bot with the bot's token
client.run("YOUR DISCORD BOT'S TOKEN")
