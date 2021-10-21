
from redbot.core import commands
from redbot.core import Config
from redbot.cogs.mutes import mutes, converters

from datetime import timedelta, datetime

import discord
import copy

class Shutup(commands.Cog):
    '''Make ur friends stfu'''
    
    def __init__(self, bot):
        # Default configuration options. Identifier is dabs#4269 discord ID
        self.config = Config.get_conf(self, identifier=152209660886253568)
        default_guild = {
            "length" : 30,      # Time the mute lasts in seconds
            "cooldown" : 0,       # How many hours until shutup can be used again
            "admin_abuse" : False # Can shutup be used on admins?
        }
        default_member = {
            "last_use" : None   # datetime when shutup was last used
        }
        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)
        self.bot = bot
        
        
    # Commands
        
    @commands.group(invoke_without_command=True, pass_context=True)
    async def shutup(self, ctx, user: discord.Member): 
        '''
        Mutes the specified user for an amount of time set by admins.
        Can only be used a certain number of times per day, also set by admins

        !shutup @user
        '''
        caller = ctx.author
        run_as = ctx.guild.owner
        length = await self.config.guild(ctx.guild).length()
        cooldown = await self.config.guild(ctx.guild).cooldown()
        time_and_reason = {"duration":timedelta(seconds=length), "reason":"shutup"}
        last_use = await self.config.member(ctx.author).last_use()
        now = datetime.now()
        if last_use is not None:
            # How long it has been since last !shutup use in seconds
            delta_hours = divmod((now - datetime.strptime(last_use, "%c")).total_seconds(), 3600)[0]
            if delta_hours < cooldown:
                await ctx.reply("Nice try kid, shutup is on cooldown :mirror:")
                await ctx.send(f"Running mute command as {str(run_as)}")
                mute_cmd = copy.deepcopy(ctx.message)
                mute_cmd.author = run_as
                mute_cmd.content = ctx.prefix + f"mute {caller} 30s shutup"
                ctx.bot.dispatch("message", mute_cmd)
            else:
                last_use = await self.config.member(ctx.author).last_use.set(now.strftime("%c"))
                await ctx.send(f"invoking mute command as {str(run_as)}")
                mute_cmd = copy.deepcopy(ctx.message)
                mute_cmd.author = run_as
                mute_cmd.content = ctx.prefix + f"mute {user} 30s shutup"
                ctx.bot.dispatch("message", mute_cmd)
        else:
            await self.config.member(ctx.author).last_use.set(now.strftime("%c"))
            await ctx.send(f"invoking mute command as {str(run_as)}")
            mute_cmd = copy.deepcopy(ctx.message)
            mute_cmd.author = run_as
            mute_cmd.content = ctx.prefix + f"mute {user} 30s shutup"
            ctx.bot.dispatch("message", mute_cmd)

        
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
    async def cooldown(self, ctx):
        '''
        Sets how many uses of shutup users have per day.
        Set to 0 for unlimited uses

        !shutup uses <0-24>
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
    
        
        