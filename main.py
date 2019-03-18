import discord
from discord.ext import commands
import math
import asyncio
from datetime import datetime
import time

from utility import getEmbedColour, getEmoji

startup_extensions = ["commands", "moderation", "events", "help", "errorhandler", "music"]


#Sql
import sqlite3

conn = sqlite3.connect("my_prefix")

#conn = sqlite3.connect("moderation")

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
    print("---------")
    print("Logged in as:")
    print(bot.user.name)
    print("Successfully connected and ready to recieve commands!")
    print("---------")
    bot.loop.create_task(status_task())
    

@bot.event
async def on_guild_join(guild):
    #Added to avoid bug where the event help message would be sent (Instead of the command help message)
    p = c.execute("SELECT prefix FROM my_prefix WHERE guild_id=?",(guild.id,)).fetchall()
    if p == [] or None:
        c.execute("INSERT INTO my_prefix VALUES(?,?)",("w/", guild.id))
        conn.commit()
        print("Prefix: " + "w/" + "Guild ID: " + str(guild.id))


    embed = discord.Embed(description=f"**{guild} successfully added me**", color=0x15c513)
    embed.set_footer(text=f"I'm currently in {len(bot.guilds)} guilds")
    await bot.get_channel(458707260978364416).send(embed=embed)


@bot.command()
async def test_cmd(ctx):
    embed = discord.Embed(title="Test", colour=0xE9A72F)
    e = await ctx.send(embed=embed)
    embed2 = discord.Embed(title="Testing", colour=0x0000FF)
    await e.edit(embed=embed2)


@bot.command()
async def prefix(ctx):
    await ctx.send(f"The servers prefix is: `{ctx.prefix}`")


@bot.command(aliases=["newprefix", "new_prefix", "set_prefix", "changeprefix"])
@commands.has_permissions(manage_server=True)
async def setprefix(ctx, prefix = None):
    if ctx.message.author.id == ctx.guild.owner.id: 
        if prefix is None:
            await ctx.send("<:redtick:506537775642968095> - You have to select a new prefix")
        else:
            if len(prefix) > 6:
                await ctx.send("<:redtick:506537775642968095> - The max prefix length is 6 characters")
            else:
                p = c.execute("SELECT prefix FROM my_prefix WHERE guild_id=?",(ctx.guild.id,)).fetchall()
                if p != [] or None:
                    c.execute("UPDATE my_prefix SET prefix = ? WHERE guild_id = ?",(prefix, ctx.guild.id))
                    conn.commit()
                else:
                    c.execute("INSERT INTO my_prefix VALUES(?,?)",(prefix, ctx.guild.id))
                    conn.commit()

                await ctx.send(f"<:greentick:506537759532515330> - Your prefix has been added to the databse and is now: `{prefix}`")
    else:
        await ctx.send("<:redtick:506537775642968095> - You have to be server owner to run this command")


@bot.command()
@commands.is_owner()
async def dbupdate(ctx):
    logs = bot.get_channel(430089438924767253)
    list_of_bot_guilds = []

    for x in ctx.bot.guilds:
        print(f"{str(x.id)}  {x.name}")
        list_of_bot_guilds.append(x.id)

    for guild in list_of_bot_guilds:
        prefix = c.execute("SELECT prefix FROM my_prefix WHERE guild_id=?",(guild,)).fetchall()

        print(prefix)
        try: 
            await logs.send(f"Server: `{guild}`\nPrefix: `{prefix[0]}`")
        except IndexError:
            await logs.send(f"Server: `{guild}`\nPrefix: `None = w/`")
            c.execute("INSERT INTO my_prefix VALUES(?,?)",("w/", guild))

    await logs.send(f"{getEmoji('green_tick')} - Succesfully updated the database")
            
    await ctx.send(f"{getEmoji('green_tick')} - Successfully updated the database")


#@bot.command()
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
        await ctx.send('<:redtick:506537775642968095> - You took to long adding a reaction')
    else:
        for extension in startup_extensions:
            bot.unload_extension(extension)
        await ctx.send("<:greentick:506537759532515330> - Successfully paused the bot")


#@bot.command()
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
        await ctx.send('<:redtick:506537775642968095> - You took to long adding a reaction')
    else:
        for extension in startup_extensions:
            bot.load_extension(extension)
        await ctx.send("<:greentick:506537759532515330> - Successfully unpaused the bot")


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
            await ctx.send(f"{getEmoji('green_tick')} - Successfully loaded {extension_name}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send(f"{getEmoji('green_tick')} - Successfully unloaded {extension_name}")


@bot.command(aliases=["reload"])
@commands.is_owner()
async def reloading(ctx, extension_name: str):
    """Reloads an extension."""
    start = time.time()
    if extension_name.lower() == "all":
        msg = await ctx.send("Reloading all extensions:")
        for x in startup_extensions:
            try:
                bot.unload_extension(x)
                bot.load_extension(x)
                end = time.time()
                total = end - start
                await msg.edit(content=f"{msg.content}\nReloaded `{x}`.")
            except (AttributeError, ImportError) as e:
                return await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))

        end = time.time()
        total = end - start
        return await ctx.send(f"{getEmoji('green_tick')} - Successfully reloaded all extensions. The process took `{round(total, 4)}s`")

    else:
        try:
            bot.unload_extension(extension_name)
            bot.load_extension(extension_name)
            end = time.time()
            total = end - start
            await ctx.send(f"{getEmoji('green_tick')} - Successfully reloaded {extension_name}. The process took `{round(total, 4)}s`")
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return


@bot.command(aliases=["oldping"])
async def testping(ctx):
    start = time.time() * 1000
    msg = await ctx.message.channel.send("Pong!")
    end = time.time() * 1000
    await msg.edit(content=f"Pong! `{(str(int(round(end-start, 0))))}ms` :ping_pong:")


@bot.command(aliases=["ut", "wafflebotut", "wafflebotuptime"])
async def uptime(ctx):
    #quick mafs
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    embed = discord.Embed(color=getEmbedColour("default"))
    embed.add_field(name="WaffleBot Uptime :calendar_spiral:", value=f"Weeks: **{weeks}**\nDays: **{days}**\nHours: **{hours}**\nMinutes: **{minutes}**\nSeconds: **{seconds}**")
    await ctx.send(embed=embed)

for extension in startup_extensions:
    try: 
        start = time.time()
        bot.load_extension(extension)
        end = time.time()
        total = end - start
        print(f"Succesfully Loaded: {extension} in {round(total, 4)}s")
    except Exception as e:
        print(e)
        
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format(extension, exc))


#Loads token from the token file
with open('token.txt') as fp:
    TOKEN = fp.read().strip()
bot.run(TOKEN, reconnect=True)
