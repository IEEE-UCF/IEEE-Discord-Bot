"""
Once a role has been made on the discord server 
then you can assign the emjoi with the roles name here 

Example Template:

reaction_roles = {
    'emoji_1':'Role_1',
    'emoji_2':'Role_2'
}

"""

reaction_roles = {
    '⚡':'EE Comp',
    '☀️':'EE Power',
    '📻':'EE RF',
    '🔊':'EE Signals',
    '💻':'CpE Comp',
    '🕹️':'CpE VLSI'
}

#channel ID of where the emebed will be sent that can be reacted on to add roles
channelIdReact = 980143575083929601

#channel ID of where the message will be sent that can be reacted on to add member role
channelIDMember = 981941557655658537

#channel ID of member count voice channel
channelIDCount = 984203513657700442

#channel ID of welcome message
channelIDWelcome = 981706501032914984

#discord embed color
hexColor = 0xF1C414

#same template of emoji to role as above but for member role
discord_member_role = {
    '<:ieee_logo_icon:982763673703546951>': 'cutIEEE'
}

#msg for member role react
discord_member_msg = {
    'msg':'Press the <:ieee_logo_icon:982763673703546951> to reveal the IEEE UCF text and voice channels!'
}

#roles that can use commands in Reaction Roles
admin_roles = [
    'President', 
    'Vice President',
    'Officer',
    'Discord Bot ree',
    'Adminastratror'
]