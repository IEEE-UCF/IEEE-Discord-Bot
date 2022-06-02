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
        
        channel = self.bot.get_channel(int(channelID))
        
        embed=discord.Embed(color=0xF1C414)
        embed.title='React for Role Assigment'
        
        desStr = ''
        keys = reaction_roles.keys()
        for i in keys:
            desStr += '{}: {}\n'.format(i, reaction_roles[i])

        embed.description=desStr
        msg = await channel.send(embed=embed)

        for i in keys:
            await msg.add_reaction(i)

    #listens for reaction on message in a channel and adds role depending on emoji
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, member):
        
        if member.id != self.bot.user.id:
            if reaction.message.channel.id == int(channelID) and reaction.emoji in reaction_roles.keys():
                role = discord.utils.get(member.guild.roles, name=reaction_roles[reaction.emoji])
                print('{} choose the role {}'.format(member.display_name), reaction_roles[reaction.emoji])
                await member.add_roles(role)

            


def setup(bot):
    bot.add_cog(ReactionRoles(bot))