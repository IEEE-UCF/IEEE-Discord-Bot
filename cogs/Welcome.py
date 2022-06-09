from discord.ext import commands
import discord
from config.config import channelIDWelcome, hexColor

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #when new member joins guild, then a welcome message is sent 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(channelIDWelcome))
        embed=discord.Embed(color=hexColor)
        embed.title = 'Welcome {}'.format(member.name)
        embed.description = 'Thank you for joining {}'.format(member.guild.name)
        embed.set_thumbnail(url = member.avatar_url)
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Welcome(bot))