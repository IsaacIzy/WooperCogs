
from redbot.core import commands
from redbot.core import Config
from redbot.cogs.mutes import mutes, converters

import discord

class Shutup(commands.Cog):
    '''Make ur friends stfu'''
    
    def __init__(self, bot):
        # Default configuration options. Identifier is dabs#4269 discord ID
        self.config = Config.get_conf(self, identifier=152209660886253568)
        default_guild = {
            "length" : "30s shutup",      # Time the mute lasts in seconds
            "uses" : 1,            # Number of time shutup can be used per day
            "admin_abuse" : False # Can shutup be used on admins?
        }
        self.config.register_guild(**default_guild)
        self.bot = bot
        
        
    # Commands
        
    @commands.group(invoke_without_command=True)
    async def shutup(self, ctx, user: discord.Member): 
        '''
        Mutes the specified user for an amount of time set by admins.
        Can only be used a certain number of times per day, also set by admins

        !shutup @user
        '''
        length = self.config.guild(ctx.guild).length()
        time_and_reason = converters.MuteTime().convert(ctx, length)
        await ctx.send(str(time_and_reason))
        await ctx.send(f"Muting {user} for {length}")
        await ctx.invoke(self.bot.get_command('mute'), user, time_and_reason)

        
    @shutup.command()
    @commands.admin()
    async def length(self, ctx, length):
        '''
        Sets how long a mute lasts for when shutup is used. Can only be used by admins

        !shutup length <30-3600>
        '''
        if length in range(30, 3601): 
            await self.config.guild(ctx.guild).length.set(length)
            await ctx.send(f"Shutup mute length set to {length} seconds")
        else:
            await ctx.send("Please enter a length between 30 and 3600")
        
        await ctx.send("it works lol")

    @shutup.command()
    @commands.admin()
    async def uses(self, ctx):
        '''
        Sets how many uses of shutup users have per day.
        Set to 0 for unlimited uses

        !shutup uses <0-10>
        '''
        await ctx.send("it works pt2 lol")
    
    @shutup.command()
    @commands.is_owner()
    async def admin_abuse(self, ctx):
        '''
        Toggles whether or not admins can be muted by shutup

        !shutup adminabuse
        ''' 
        # TODO
        
    # Utility functions
    
        
        