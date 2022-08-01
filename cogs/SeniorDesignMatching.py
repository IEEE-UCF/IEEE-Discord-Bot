from unicodedata import category
from discord.ext import commands
import discord
from config.config import channelIDSD, admin_roles
SDcategory = channelIDSD

class SeniorDesignMatching(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    #command to create role and text channel for senior design and if those already exist then the member who
    #uses the command gets the role to access the text channel already created
    @commands.command(name='sdm')
    async def sdm_command(self, ctx, semesters, year):

        #Sets the user's response for semesters to lowercase
        semesters = str(semesters.lower())
        year = str(year)
        cases = ['fasp', 'spfa', 'spsu', 'sufa']

        yearsList = []
        for i in range(2022, 2122):
            yearsList.append(str(i))

        #If the user enters a valid semester and year 
        if semesters in cases and year in yearsList:
            semesYear = semesters + ' ' + year
            semesYearH = semesters + '-' + str(year)
            
            #If the current role exists, give the user the current role
            if discord.utils.get(ctx.guild.roles, name=semesYear) != None:
                role = discord.utils.get(ctx.guild.roles, name=semesYear)
                await ctx.author.add_roles(role)
                print('Only Role Given')

                for channels in ctx.guild.channels:
                    if str(channels) == str(semesYearH):
                        channel = channels

            #If the current doesn't exist, create a new channel, give user the role, and adjust permissions of channel 
            #so only user will role can see the channel    
            else:
                await ctx.guild.create_role(name=semesYear)
                
                sdmRole = discord.utils.get(ctx.guild.roles, name=semesYear)
                everyone = discord.utils.get(ctx.guild.roles, name='@everyone')
                botrole = discord.utils.get(ctx.guild.roles, name='ieeeucf bot')

                #Sets permissions to channel 
                overwrites = {
                    everyone: discord.PermissionOverwrite(view_channel=False),
                    sdmRole: discord.PermissionOverwrite(view_channel=True),
                    botrole: discord.PermissionOverwrite(view_channel=True)
                }

                #Create channel and put in SD matching
                category = discord.utils.get(ctx.guild.categories, name='📚SD Matching📚')
                
                channel = await ctx.guild.create_text_channel('{}'.format(semesYear),category=category, overwrites=overwrites)
                
                await ctx.author.add_roles(sdmRole)
                print('Channel and Role created')

            await channel.send('Welcome {} your Senior Design Matching Channel'.format(ctx.author.mention))
        
        else:
            await ctx.channel.send('Your arguments were not correct. \nFormart for Fall 2024-Spring 2025 must be: -sdm fasp 2024')

    #removes senior design role from user that calls it and the role is determined by the parameters
    @commands.command(name='sdmRemove')
    async def sdmRemove_command(self, ctx, semesters, year):

        semesters = str(semesters.lower())
        cases = ['fasp', 'spfa', 'spsu', 'sufa']
        if semesters in cases:
            semesYear = semesters + ' ' + str(year)

            if discord.utils.get(ctx.guild.roles, name=semesYear) != None:
                role = discord.utils.get(ctx.guild.roles, name=semesYear)
                await ctx.author.remove_roles(role)
                

    #deletes the text channel and role form the specified parameters around senior design
    @commands.command(name='sdmDelete')
    async def sdmDelete_command(self, ctx, semesters, year):

        user_role = str(ctx.author.top_role)
        if user_role in admin_roles:

            semesters = str(semesters.lower())
            cases = ['fasp', 'spfa', 'spsu', 'sufa']
            if semesters in cases:

                semesYearH = semesters + '-' + str(year)
                semesYear = semesters + ' ' + str(year)
                guild = ctx.guild 
                for channel in guild.channels:
                    if str(channel) == str(semesYearH):
                        await channel.delete()
                        print('{} Channel deleted'.format(semesYear))
                if discord.utils.get(ctx.guild.roles, name=semesYear) != None:
                    role = discord.utils.get(ctx.guild.roles, name=semesYear)
                    await role.delete()
                    print('{} Role deleted'.format(semesYear))


def setup(bot):
    bot.add_cog(SeniorDesignMatching(bot))