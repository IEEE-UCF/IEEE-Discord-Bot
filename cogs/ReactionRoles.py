from discord.ext import commands
from discord.utils import get
import discord
from config.config import channelID, reaction_roles


class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #when bot runs send embed in read only channel for members to react on embed to assign roles to a member
    @commands.Cog.listener()
    async def on_ready(self):
        #channelID = 974865668262477865
        channel = self.bot.get_channel(int(channelID))
        
        embed=discord.Embed(color=0xFFEA00)
        embed.title='React for Role Assigment'
        embed.description='Test Role: :fire:'
        await channel.send(embed=embed)

    #listens for reaction on message in a channel and adds role depending on emoji
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, member):
        #channelID = 974865668262477865
        if reaction.message.channel.id == int(channelID) and reaction.emoji in reaction_roles.keys():
            Role = discord.utils.get(member.guild.roles, name=reaction_roles[reaction.emoji])
            await member.add_roles(Role)
            


def setup(bot):
    bot.add_cog(ReactionRoles(bot))