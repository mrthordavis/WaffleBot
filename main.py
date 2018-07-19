import discord
from discord.ext import commands
import math
import asyncio
import random
from datetime import datetime

bot = commands.Bot(command_prefix = "w/", owner_id = 322449414142558208)
bot.launch_time = datetime.utcnow()

startup_extensions = ["commands", "staff", "events", "music", "admin", "help"]

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name=f"On {len(bot.guilds)} Servers"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="Prefix = w/"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"With {len(bot.users)} Users"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="w/help"))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print("Successfully connected and ready to recieve commands!")
    print("---------")
    bot.loop.create_task(status_task())

@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    if ctx.message.author.id == 322449414142558208:
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        embed = discord.Embed(color=0x15c513)
        embed.add_field(name="Cog loaded.", value=f"Successfully loaded {extension_name}!")
        send = await ctx.send(embed=embed)
        await send.add_reaction(emoji="👌")
    else:
        error = discord.Embed(color=0xE73C24)
        error.add_field(name="Error:", value="You don't have permission to do that!")
        await ctx.send(embed=error)

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if ctx.message.author.id == 322449414142558208:
        bot.unload_extension(extension_name)
        embed = discord.Embed(color=0x15c513)
        embed.add_field(name="Cog unloaded", value=f"Successfully unloaded {extension_name}")
        send = await ctx.send(embed=embed)
        await send.add_reaction(emoji="👌")
    else:
        error = discord.Embed(color=0xE73C24)
        error.add_field(name="Error:", value="You don't have permission to do that!")
        await ctx.send(embed=error)

@bot.command(aliases=["reload"])
async def reloading(ctx, extension_name : str):
    """Reloads an extension."""
    if ctx.message.author.id == 322449414142558208:
        try:
            bot.unload_extension(extension_name)
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        else:
            embed = discord.Embed(color=0x15c513)
            embed.add_field(name="Cog Reloaded", value=f"Successfully reloaded {extension_name}")
            send = await ctx.send(embed=embed)
            await send.add_reaction(emoji="👌")
    else:
        error = discord.Embed(color=0xE73C24)
        error.add_field(name="Error:", value="You don't have permission to do that!")
        await ctx.send(embed=error)

@bot.command(aliases=["ut", "wafflebotut", "wafflebotuptime"])
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    embed = discord.Embed(color=0xE9A72F)
    embed.add_field(name="WaffleBot Uptime :calendar_spiral:", value=f"Weeks: **{weeks}**\nDays: **{days}**\nHours: **{hours}**\nMinutes: **{minutes}**\nSeconds: **{seconds}**")
    await ctx.send(embed=embed)

for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

with open('token.txt') as fp:
    TOKEN = fp.read().strip()
bot.run(TOKEN, reconnect=True)