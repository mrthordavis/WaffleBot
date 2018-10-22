import discord
from discord.ext import commands

class ErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        print(error)
        error = error.__cause__ or error
        await self.bot.get_channel(491258907050639390).send(f"Command: `{ctx.message.content}`\nServer: `{ctx.message.guild.name}`\nChannel: `{ctx.message.channel}`\nAuthor: `{ctx.message.author}` ```{error}```")
        if isinstance(error, discord.Forbidden):
            if "admin" in str(ctx.command):
                return
            else:
                await ctx.send(":x: - I don't have enough perms to execute that command")

        elif isinstance(error, commands.CommandNotFound):
            #Commands I'm reworking
            if "warn" in str(ctx.command):
                await ctx.send(":x: - This command is currently getting reworked")
            elif "clearwarns" in str(ctx.command):
                await ctx.send(":x: - This command is currently getting reworked")
            elif "mute" in str(ctx.command):
                await ctx.send(":x: - This command is currently getting reworked")
            elif "unmute" in str(ctx.command):
                await ctx.send(":x: - This command is currently getting reworked")
            else:
                await ctx.message.add_reaction(emoji="❓")
                print(f"I couldn't find the command named: {ctx.message.content}")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(":x: - You don't have enough perms to execute that command")

        elif isinstance(error, commands.NotOwner):
            await ctx.send(":x: - **You do not own this bot**")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
