from distutils.dir_util import remove_tree
from os import remove
from discord.ext import commands
from discord.utils import get
import discord
from config.config import channelIdReact, reaction_roles, admin_roles, channelIDMember, discord_member_msg, discord_member_role

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    reactRoleMsg = 0        #holds message id of reaction role embed
    reactMemberMsg = 0      #holds message id of reaction member message
    
    #command to send or delete the react embed for roles and the member role message
    #ie. -reactEmbed [roles/member] [send/delete]
    @commands.command(name='reactEmbed', aliases= ['re'])
    async def reactEmbed_command(self, ctx, type, action):
        user_role = str(ctx.author.top_role) #gets top role of user calling command

        if user_role in admin_roles: #checks with which roles have access to this command in admin_roles in config/config.py

            if action == 'send': #checks if second argument (action) is send 

                if type == 'roles': #checks if first argument (type) is roles
                    if self.reactRoleMsg == 0: #checks if this command has already been run so as to not have duplicate messages sent
                        channel = self.bot.get_channel(int(channelIdReact))
                        embed=discord.Embed(color=0xF1C414)
                        embed.title='React for Role Assigment'

                        desStr = ''
                        keys = reaction_roles.keys()
                        for i in keys:
                            desStr += '{}: {}\n'.format(i, reaction_roles[i])

                        embed.description=desStr
                        msg = await channel.send(embed=embed) #sends embed

                        for i in keys:
                            await msg.add_reaction(i) #adds reaction to embed

                        await ctx.channel.send('React Embed has been created')
                        print('React Embed has been created')
                        self.reactRoleMsg = msg
                    else:
                        await ctx.channel.send('React Embed has already been created, it must be deleted first (-reactEmbed roles delete)')
                        print('React Embed has already been created')

                elif type =='member': #checks if first argument (type) is member
                    if self.reactMemberMsg == 0: #checks if this command has already been run so as to not have duplicate messages sent
                        channel = self.bot.get_channel(int(channelIDMember))
                        embed = discord.Embed(color=0xF1C414)
                        embed.title = 'Server Access'
                        embed.description = discord_member_msg['msg']

                        msg = await channel.send(embed=embed) #sends message

                        keys = discord_member_role.keys()
                        for i in keys:
                            await msg.add_reaction(i) #adds reaction to embed

                        await ctx.channel.send('Member React has been created')
                        print('Member React has been created')
                        self.reactMemberMsg = msg
                    else:
                        await ctx.channel.send('Member React has already been created, it must be deleted first (-reactEmbed member delete)')
                        print('Member React has already been created')

            elif action == 'delete': #checks if second argument (action) is delete

                if type == 'roles': #checks if first argument (type) is roles
                    if self.reactRoleMsg != 0: #checks if this command has already been run so as to not try and delete something that doesn't exist
                        await self.reactRoleMsg.delete() #deletes embed
                        await ctx.channel.send('React Embed has been deleted')
                        print('React Embed has been deleted')
                        self.reactRoleMsg = 0
                    else:
                        await ctx.channel.send('React Embed has already been deleted')
                        print('React Embed has already been deleted')

                elif type == 'member': #checks if first argument (type) is member
                    if self.reactMemberMsg != 0: #checks if this command has already been run so as to not try and delete something that doesn't exist
                        await self.reactMemberMsg.delete() #deletes embed
                        await ctx.channel.send('Member React has been deleted')
                        print('Member React has been deleted')
                        self.reactMemberMsg = 0
                    else:
                        await ctx.channel.send('React Embed has already been deleted')
                        print('Member React has already been deleted')

        else:
            print('not authorized') #send print in console log that someone without the permissions tried to use this command
            

    #listens for reaction on message in a channel and adds role depending on emoji
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, member):

        if member.id != self.bot.user.id and (reaction.message == self.reactRoleMsg or reaction.message == self.reactMemberMsg): #make sure the bot can't add a role and that it is one of the two channels that reactions for roles happen
            
            roles = [] #makes a list of the roles of who reacted
            for i in range(len(member.roles)):
                roles.append(member.roles[i])
        
            if reaction.message == self.reactRoleMsg and reaction.emoji in reaction_roles.keys(): #major roles
                role = discord.utils.get(member.guild.roles, name=reaction_roles[reaction.emoji]) #grab role
                if role in roles: #see if they already have the role, if so then remove their role and if not then add the role to the member
                    print('{} removed a role'.format(member.name))
                    await member.remove_roles(role)
                else:    
                    print('{} choose a role'.format(member.name))
                    await member.add_roles(role)
                await self.reactRoleMsg.remove_reaction(reaction.emoji, member) #remove reaction from message

            elif reaction.message == self.reactMemberMsg and str(reaction.emoji) in discord_member_role.keys(): #member role
                role = discord.utils.get(member.guild.roles, name=discord_member_role[str(reaction.emoji)]) #grab role
                if role in roles: #see if they already have the role, if so then remove their role and if not then add the role to the member
                    print('{} removed a role'.format(member.name))
                    await member.remove_roles(role)
                else:    
                    print('{} choose a role'.format(member.name))
                    await member.add_roles(role)
                await self.reactMemberMsg.remove_reaction(reaction.emoji, member) #remove reaction from message

def setup(bot):
    bot.add_cog(ReactionRoles(bot))