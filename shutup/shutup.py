from redbot.core import commands

class Shutup(commands.Cog):
    '''Make ur friends stfu'''
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def shutup(self, ctx):
        '''
        Mutes the specified user for an amount of time set by admins.
        Can only be used a certain number of times per day, also set by admins
        '''
        await ctx.send("No you shutup!")