from nis import cat
from unicodedata import category
from discord.ext import commands
import discord
from config.config import yearList
SDcategory = 987017084812787742


class SeniorDesignMatching(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'sdm')
    async def sdm_command(self, ctx, semesters, year):

        #Sets the user's response for semesters to lowercase
        semesters = str(semesters.lower())
        cases = ['fasp', 'spfa', 'spsu', 'sufa']
        year = str(year)
        
        yearList = []
        for i in range(2022, 2122):
            yearList.append(str(i))


        #If the user enters a valid semester and year 
        if semesters in cases and year in yearList:

            semesYear = semesters + ' ' + year

            #If the current role exists, give the user the current role
            if discord.utils.get(ctx.guild.roles, name = semesYear) != None:
                role = discord.utils.get(ctx.guild.roles, name = semesYear)
                await ctx.author.add_roles(role)
                channel = discord.utils.get(ctx.guild.text_channel, name = semesYear)
                await channel.send('Welcome @{} to your Senior Design Matching channel'.format(ctx.author.display_name))
            
            #If the current doesn't exist, create a new channel, give user the role, and adjust permissions of channel 
            #so only user will role can see the channel
            else:
                await ctx.guild.create_role(name=semesYear)
                sdmRole = discord.utils.get(ctx.guild.roles, name = semesYear)
                everyone = discord.utils.get(ctx.guild.roles, name = '@everyone')
                botRole = discord.utils.get(ctx.guild.roles, name = 'ieee bot')

                #Sets permissions to channel 
                overwrites ={
                    sdmRole: discord.PermissionOverwrite(view_channel=True),
                    everyone: discord.PermissionOverwrite(view_channel=False),
                    botRole: discord.PermissionOverwrite(view_channel=True)
                }

                #Create channel and put in SD matching
                category = discord.utils.get(ctx.guild.categories, name="📚SD Matching📚")
                channel = await ctx.guild.create_text_channel('{}'.format(semesYear), category=category, overwrites=overwrites)
                await ctx.author.add_roles(sdmRole)
                await channel.send('Welcome @{} to your Senior Design Matching channel'.format(ctx.author.display_name))
        
        else:
            await ctx.channel.send('Your arguments were not corret.\nFormat  for Fall 2024-Spring 2025 must be: -sdm fasp 2024')

def setup(bot):
    bot.add_cog(SeniorDesignMatching(bot))