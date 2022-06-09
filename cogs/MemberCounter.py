from abc import update_abstractmethods
from turtle import update
from discord.ext import commands
from config.config import channelIDCount, admin_roles

class MemberCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    #command to update member counter voice channel name with an updated amount of members in the discord server
    @commands.command(name='memberCounter', aliases= ['mc'])
    async def memberCounter_command(self, ctx):
        user_role = str(ctx.author.top_role)
        if user_role in admin_roles:
            count = ctx.guild.member_count
            await self.updateMemberCount(count)
            await ctx.channel.send('Member Count Updated')

    #listens for someone to join the server and then updates the member counter
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print('{} joined {}'.format(member.name, member.guild))    
        count = member.guild.member_count
        await self.updateMemberCount(count)

    #listens for someone to leave the server and then updates the member counter
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print('{} left {}'.format(member.name, member.guild))    
        count = member.guild.member_count
        await self.updateMemberCount(count)
   
   #function called by the other functions in this cog to update the voice channel with the member count
    async def updateMemberCount(self, count):
        vc = self.bot.get_channel(int(channelIDCount)) #grabs channel from channel id
        print('Member Count Updated')
        await vc.edit(name='Member Count: {}'.format(count)) #edits channel name with updated count of members in the server

def setup(bot):
    bot.add_cog(MemberCounter(bot))


