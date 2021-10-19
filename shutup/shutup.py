from redbot.core import commands
from redbot.core import Config

class Shutup(commands.Cog):
    '''Make ur friends stfu'''
    
    def __init__(self, bot):
        # Default configuration options. Identifier is dabs#4269 discord ID
        self.config = Config.get_conf(self, identifier=152209660886253568)
        default_guild = {
            "length" : 30,      # Time the mute lasts in seconds
            "uses" : 1,            # Number of time shutup can be used per day
            "admin_abuse" : false # Can shutup be used on admins?
        }
        self.config.register_guild(**default_guild)
        self.bot = bot
        
    @commands.command(name="shutup")
    async def shutup(self, ctx):
        '''
        Mutes the specified user for an amount of time set by admins.
        Can only be used a certain number of times per day, also set by admins
        '''
        await ctx.send("No you shutup!")
        
    @commands.command(name="shutup len")
    @commands.admin()
    async def shutup_len(self, ctx):
        '''
        Sets how long a mute lasts for when shutup is used. Can only be used by admins
        '''
        await ctx.send("it works lol")
        