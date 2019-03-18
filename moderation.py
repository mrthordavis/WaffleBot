import discord
from discord.ext import commands
import inspect #Used for the source command
import psutil #Stats command
import datetime #Used for boot date in w/stats
import time #Used for execution time

from utility import getEmbedColour, getEmoji, guild_owner

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{getEmoji('red_tick')} - You forgot to mention a user")
        else:
            await user.kick()
            await ctx.send(f"{getEmoji('green_tick')} - Successfully kicked: {user.name}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{getEmoji('red_tick')} - You forgot to mention a user")
        else:
            await user.ban()
            await ctx.send(f"{getEmoji('green_tick')} - Successfully banned: {user.name}")

    @commands.command(aliases=["command", "code"])
    @commands.is_owner()
    async def source(self, ctx, *, text: str):
        try:
            """Shows source code of a command."""
            nl2 = '`'
            nl = f"``{nl2}"
            source_thing = inspect.getsource(self.bot.get_command(text).callback)
            await ctx.send(f"{nl}py\n{source_thing[:1990]}{nl}")
            if len(source_thing) > 1990:
                await ctx.send(f"{nl}py\n{source_thing[1990:3980]}{nl}")
                if len(source_thing) > 3980:
                    await ctx.send(f"{nl}py\n{source_thing[3980:5970]}{nl}")
                    if len(source_thing) > 5970:
                        await ctx.send(f"{nl}py\n{source_thing[5970:7960]}{nl}")
        except AttributeError:
            await ctx.send(f"{getEmoji('red_tick')} - Please enter a valid command name")


    @commands.command(aliases=["raidclean", "cleanraid", "clearup"])
    @commands.is_owner()
    async def cleanup(self, ctx, channel: str = None):
        if channel is None:
            await ctx.send(f"{getEmoji('red_tick')} - You didn't specify a channel name")
        else:
            counter = 0
            await ctx.send(f"Cleanup of channels named `{channel}` is beggining!")
            for x in ctx.message.guild.channels:
                if x.name == channel:
                    counter += 1
                    await x.delete()
                    time.sleep(2)
                    print(f"{counter} channel(s) deleted")
            await ctx.send(f"{getEmoji('green_tick')} - Successfully deleted {counter} channel(s) named `{channel}`")


    @commands.command()
    @commands.check(guild_owner)
    async def bot_leave(self, ctx):
        await ctx.send("Leaving the server")
        await ctx.guild.leave()
        print(f"I left {ctx.guild.name}")


    @commands.command()
    async def stats(self, ctx):
        start = time.time()
        msg = await ctx.send("Fetching stats please be patient :slight_smile:")

        cpu_percentage = psutil.cpu_percent()

        if cpu_percentage > 10:
            colour = discord.Colour(getEmbedColour("red"))
        elif cpu_percentage > 5: #Find a different colour
            colour = discord.Colour(getEmbedColour("yellow"))
        else:
            colour = discord.Colour(getEmbedColour("green"))
        embed = discord.Embed(color=colour)
        embed.set_author(name="RPI 3 Model B ")

        embed.add_field(name="CPU Usage:", value=f"`{cpu_percentage}%`")

        embed.add_field(name="Cpu Cores:", value=f"`{psutil.cpu_count()}`")

        embed.add_field(name="Clock Speed:", value=f"`{psutil.cpu_freq()[0]} Mhz`")

        embed.add_field(name="Max Clock Speed:", value=f"`{psutil.cpu_freq()[2]} Mhz`")

        quick_mafs = psutil.virtual_memory()[2] / 1000000000
        embed.add_field(name="RAM Usage:", value=f"`{str(quick_mafs)[:4]}%`")

        mafs = psutil.virtual_memory()[0] / 1000000000
        embed.add_field(name="Total RAM:", value=f"`{str(mafs)[:4]} gb`")

        embed.add_field(name="Storage Used:", value=f"`{psutil.disk_usage('/')[3]}%`")
        key_name = 'bcm2835_thermal'  
        try:
            sensors = psutil.sensors_temperatures()[key_name]
            embed.add_field(name="CPU Temp:", value=f"`{sensors[0].current}°C`")
        except AttributeError:
            embed.add_field(name="CPU Temp:", value=f"`Not avaliable`")

        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%d-%m %H:%M:%S")
        embed.add_field(name="Boot Date:", value=f"`{boot_time}`")

        end = time.time()
        total = end - start

        embed.set_footer(text=f"Results returned in {round(total, 2)}s")

        await msg.delete()
        await ctx.send(embed=embed)


    @commands.command(aliases=["purge", "nuke"])
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, number: int = None):
        if number is None:
            await ctx.send(f"{getEmoji('red_tick')} - You didn't specify the amount of messages")
        else:
            await ctx.channel.purge(limit=number+1)
            msg = await ctx.send(f"{getEmoji('green_tick')} - Successfully deleted {number} messages")
            time.sleep(7)
            await msg.delete()


    @commands.command(aliases=["kill", "quit", "logout", "kys"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send(f"{getEmoji('green_tick')} - The bot was successfully shut down")
        print("The bot was successfully shut down!")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Staff(bot))
