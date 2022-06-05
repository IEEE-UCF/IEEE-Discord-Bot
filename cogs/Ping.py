from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #when messge with correct prefix (-ping) bot sends message pong
    @commands.command(name='ping')
    async def ping_command(self, ctx):
        print('Ping Command called')
        await ctx.channel.send('pong')
    
    @commands.command(name='bing')
    async def bing_command(self, ctx):
        print('Bing Command called')
        await ctx.channel.send('bong')

    @commands.command(name='ding')
    async def ding_command(self, ctx):
        print('Ding Command called')
        await ctx.channel.send('dong')
        


def setup(bot):
    bot.add_cog(Ping(bot))