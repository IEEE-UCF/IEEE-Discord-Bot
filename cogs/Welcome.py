from discord.ext import commands
import discord

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #when new member joins guild, then a welcome message is sent 
    @commands.Cog.listener()
    async def on_message_join(self, memeber):
        channel = self.get_channel(980143575083929601)
        embed=discord.Embed(color=0xF1C414)
        embed.title = 'Welcome {memeber.name}'
        embed.description = 'Thank you for joining {memeber.guild.name}'
        embed.set_thumbnail(url = memeber.avatar_url)
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Welcome(bot))