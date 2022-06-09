from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='-', help_command=None, intents=intents)

#print to console that Bot is logged in
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#name of .py file of a cog in cogs file goes into cogs then if the .py name is main then load all cogs
cogs = ['Ping', 'Welcome', 'ReactionRoles','MemberCounter']

if __name__ == '__main__':
    for cog in cogs:
        client.load_extension('cogs.'+cog)


#load env file and use token to run bot
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))