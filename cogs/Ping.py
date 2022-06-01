from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #when messge with correct prefix (?ping) bot sends message pong
    @commands.command(name='ping')
    async def ping_command(self, ctx):
        print('Ping Command called')
        await ctx.channel.send('pong')



def setup(bot):
    bot.add_cog(Ping(bot))