import discord
from discord.ext import commands
import asyncio

class GeneralCommands():
    def __init__(self, bot):
        self.bot = bot

    #Check example:
    """def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '\N{BLACK RIGHTWARDS ARROW}'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("You spent to long adding a reaction")
            await help.delete()
            await ctx.message.delete()

        if reaction.emoji == "\N{BLACK RIGHTWARDS ARROW}":
            #do something"""

def setup(bot):
    bot.add_cog(GeneralCommands(bot))