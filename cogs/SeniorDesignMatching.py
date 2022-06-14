from discord.ext import commands

class SeniorDesignMatching(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    #@commands.command(name = 'sdm')

def setup(bot):
    bot.add_cog(SeniorDesignMatching(bot))