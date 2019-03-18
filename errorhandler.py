import discord
import traceback
from discord.ext import commands
import logging #Still have to learn this

from utility import getEmoji

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        error = error.__cause__ or error
        await self.bot.get_channel(491258907050639390).send(f"Command: `{ctx.message.content}`\nServer: `{ctx.message.guild.name}`\nChannel: `{ctx.message.channel}`\nAuthor: `{ctx.message.author}` ```{error}```")
        if isinstance(error, discord.Forbidden):
            if "admin" in str(ctx.command):
                return
            else:
                await ctx.send(f"{getEmoji('red_tick')} - I don't have enough perms to execute that command")

        elif isinstance(error, commands.CommandNotFound):
            #Commands I'm reworking
            if "warn" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - This command is currently getting reworked")
            elif "clearwarns" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - This command is currently getting reworked")
            elif "mute" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - This command is currently getting reworked")
            elif "unmute" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - This command is currently getting reworked")
            else:
                await ctx.message.add_reaction(emoji="❓")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{getEmoji('red_tick')} - You don't have enough perms to execute that command")

        elif isinstance(error, commands.BotMissingPermissions):
            if "help" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - I need the `add_reactions` permission in order to do that")
                return
            elif "ftn" in str(ctx.command):
                await ctx.send(f"{getEmoji('red_tick')} - I need the `add_reactions` permission in order to do that")
                return
            await ctx.send(f"{getEmoji('red_tick')} - I don't have enough permissions to do that")

        elif isinstance(error, commands.NotOwner):
            await ctx.send(f"{getEmoji('red_tick')} - You do not own this bot")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{getEmoji('red_tick')} - {error}")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
