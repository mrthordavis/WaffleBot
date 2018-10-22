import discord
from discord.ext import commands
import math
import asyncio
from datetime import datetime

startup_extensions = ["commands", "staff", "events", "music", "admin", "help", "errorhandler"]

#Sql
import sqlite3

conn = sqlite3.connect("my_prefix")

conn = sqlite3.connect("moderation")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS moderation(
    user_id BIGINT PRIMARY KEY,
    guild_id BIGINT,
    warns_int INT)
""")

conn.commit()

def bot_prefix(bot, ctx):
    #defining if not in guild to use prefix
    if not ctx.guild:
         return "w/"
    else:
        #gotta create the table
        c.execute("""CREATE TABLE IF NOT EXISTS my_prefix(
            prefix VARCHAR,
            guild_id BIGINT PRIMARY KEY)
            """)
        #loading the prefix
        xprefix = c.execute("SELECT prefix FROM my_prefix WHERE guild_id=?",(ctx.guild.id,)).fetchall()
        #If No Value
        if xprefix == None:
            return "w/"
        if xprefix == []:
            return "w/"

        #If it has a value
        else:
            #Makes it so that it returns the prefix, not tuple
            return xprefix[0]

def guild_owner(ctx):
    return ctx.message.guild.owner

bot = commands.Bot(command_prefix = bot_prefix, owner_id = 322449414142558208, case_insensitive=True)
bot.launch_time = datetime.utcnow()

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name=f"On {len(bot.guilds)} Servers"))
        await asyncio.sleep(10)
        #await bot.change_presence(activity=discord.Game(name="Prefix = w/"))
        #await asyncio.sleep(10)
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

@bot.command(aliases=["newprefix", "new_prefix", "set_prefix", "changeprefix"])
@commands.check(guild_owner)
async def setprefix(ctx, prefix = None):
    if prefix is None:
        await ctx.send(":x: - You have to select a new prefix")
    else:
        if len(prefix) > 6:
            await ctx.send(":x: - The max prefix length is 6 characters")
        else:
            p = c.execute("SELECT prefix FROM my_prefix WHERE guild_id=?",(ctx.guild.id,)).fetchall()
            if p != [] or None:
                c.execute("UPDATE my_prefix SET prefix = ? WHERE guild_id = ?",(prefix, ctx.guild.id))
                conn.commit()
            else:
                c.execute("INSERT INTO my_prefix VALUES(?,?)",(prefix, ctx.guild.id))
                conn.commit()

            await ctx.send(f":white_check_mark: - Your prefix has been added to the databse and is now: `{prefix}`")

@bot.command()
@commands.is_owner()
async def botpause(ctx):
    msg = await ctx.send("Are you sure you want to pause the bot?")
    await msg.add_reaction(emoji="✅")
    await msg.add_reaction(emoji="❌")

    def check(_reaction, _user):
        return _user == ctx.message.author and str(_reaction.emoji) == '✅'

    try:
        _reaction, _user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(':x: - You took to long adding a reaction')
    else:
        for extension in startup_extensions:
            bot.unload_extension(extension)
        await ctx.send(":white_check_mark: - Successfully paused the bot")

@bot.command()
@commands.is_owner()
async def botunpause(ctx):
    msg = await ctx.send("Are you sure you want to unpause the bot?")
    await msg.add_reaction(emoji="✅")
    await msg.add_reaction(emoji="❌")

    def check(_reaction, _user):
        return _user == ctx.message.author and str(_reaction.emoji) == '✅'

    try:
        _reaction, _user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(':x: - You took to long adding a reaction')
    else:
        for extension in startup_extensions:
            bot.load_extension(extension)
        await ctx.send(":white_check_mark: - Successfully unpaused the bot")

@bot.command()
@commands.is_owner()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    if ctx.guild.me.guild_permissions.add_reactions:
            try:
                bot.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            embed = discord.Embed(color=0x15c513)
            embed.add_field(name="Cog loaded.", value=f"Successfully loaded {extension_name}!")
            send = await ctx.send(embed=embed)
            #This part needs testing
            if ctx.guild.me.guild_permissions.add_reactions:
                await send.add_reaction(emoji="👌")
            else:
                return

@bot.command()
@commands.is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    embed = discord.Embed(color=0x15c513)
    embed.add_field(name="Cog unloaded", value=f"Successfully unloaded {extension_name}")
    send = await ctx.send(embed=embed)
    if ctx.guild.me.guild_permissions.add_reactions:
        await send.add_reaction(emoji="👌")
    else:
        return

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
    #quick mafs
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

#Loads token from the token file
with open('token.txt') as fp:
    TOKEN = fp.read().strip()
bot.run(TOKEN, reconnect=True)
