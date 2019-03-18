import discord
import asyncio
import random
import traceback
from discord.ext import commands

from utility import getEmbedColour

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #Need to make an exception on this
    """async def on_guild_channel_create(self, channel):
        if channel.me.guild_permissions.administrator:
            await channel.send("First!")"""


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        embed = discord.Embed(description=f"**{guild} successfully removed me**", color=0xE73C24)
        embed.set_footer(text=f"I'm currently in {len(self.bot.guilds)} guilds")
        await self.bot.get_channel(458707260978364416).send(embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        bot_count = sum(m.bot for m in member.guild.members)
        human_count = len(member.guild.members) - bot_count

        if member.guild.id == 337291099129511937:
            embed = discord.Embed(color=0x0098FD)
            embed.add_field(name="Welcome to Gamers Hangout!", value=f"Hello {member.name}! Make sure to check out the <#444489468012003338>")
            embed.set_footer(icon_url=member.avatar_url, text=f"You're the {human_count}th member")
            await self.bot.get_channel(444483955119357962).send(embed=embed)
            role = discord.utils.get(member.guild.roles, id=444490535076626442)
            await member.add_roles(role)

        if member.guild.id == 414493368861589514:
            embed = discord.Embed(title="New User Joined", colour=0x15c513)
            embed.add_field(name="Name", value=f"{member.name}")
            embed.add_field(name="Joined", value=str(member.joined_at)[:19])
            embed.add_field(name="Created at", value=str(member.created_at)[:19])
            embed.add_field(name="User ID", value=member.id)
            embed.add_field(name="User Discriminator", value=f"#{member.discriminator}")
            if member.bot:
                embed.add_field(name="Bot", value="True")
            else:
                embed.add_field(name="Bot", value="False")
            await self.bot.get_channel(430089438924767253).send(embed=embed)
        else:
            return


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id == 414493368861589514:
            if message.author.id == 430365624217108484:
                return
            else:
                embed = discord.Embed(title="Message Deletion", description=f"**{message.author}** deleted a message in <#{message.channel.id}>\n**Content:** `{message.content}`", colour=0x15c513)
                await self.bot.get_channel(430089438924767253).send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message):
        #WaffleBot Server
        if message.channel.id == 417743778925903872:
            if message.content.upper() != "!ACCEPT" and message.content.upper() != "!DECLINE":
                if message.author.id == 322449414142558208:
                    pass
                else:
                    await message.delete()
            elif message.content.upper().startswith("!ACCEPT"):
                find_role = discord.utils.get(message.guild.roles, id=417057802528358402)
                await message.author.add_roles(find_role)
                embed = discord.Embed(color=0xE9A72F)
                embed.add_field(name="Welcome to WaffleBot Support Server!", value=f"Hello {message.author.mention}! Make sure to check out the <#417743778925903872>")
                owneravi = self.bot.get_user(322449414142558208)
                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                await self.bot.get_channel(414493369625214987).send(embed=embed)
                await asyncio.sleep(2)
                await message.delete()
            elif message.content.upper().startswith("!DECLINE"):
                await message.author.kick()
                await asyncio.sleep(2)
                await message.delete()

        elif message.content.upper().startswith("BIG SHAQ"):
            await message.channel.send(random.choice(["2 + 2 = 4 - 1 that's 3 quick maths",
                                                                    "Smoke trees",
                                                                    "Man's not hot",
                                                                    "The things goes skrrrrra, pa pa ka ka ka",
                                                                    "Babes, man's not hot",
                                                                    "Hop out the four-door with the .44, it was one, two, three and four",
                                                                    "Skidika-pap-pap",
                                                                    "No ketchup, just sauce, raw sauce",
                                                                    "Rice Krispies, hold tight my girl, Whitney"])) #Add more commands

        elif message.content.upper() == "PREFIX":
            prefix = await self.bot.get_prefix(message)
            prefix = prefix[0]
            print(prefix[0])
            await message.channel.send(f"The current prefix in the guild is: `{prefix}`")

        #Should be working
        elif message.content.upper() == "W/HELP":
            prefix = await self.bot.get_prefix(message)
            prefix = prefix[0]
            #if prefix == "w":
                #return
            if prefix != "w/":


                #testing embed
                """generalCommands1 = discord.Embed(color=getEmbedColour("default"))
                generalCommands1.set_author(name="[1/4]")
                generalCommands1.add_field(name="General Commands:pushpin:", value=
                "**w/ping**\n**w/roles**\n**w/info *<user>**\n**w/serverinfo**\n**w/uptime**\n**w/links**\n**w/google <search>**\n**w/createinvite *<uses>**\n**w/wiki <search>**\n**w/ftn <platform> <username>**\n**w/translate <text>**".replace("**", ""), inline=False)
                generalCommands1.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                generalCommands1.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                generalCommands1.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")"""


                #The different embeds
                generalCommands1 = discord.Embed(color=getEmbedColour("default"))
                generalCommands1.set_author(name="[1/4]")
                generalCommands1.add_field(name="General Commands:pushpin:", value="**w/ping** Pong! :ping_pong:\n**w/roles** - Lists all roles in the sever\n**w/setprefix <new prefix>** - Changes the default prefix\n**w/info *<user>** - Shows some information about you\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Shows the bots current uptime\n**w/links** - Get the support server and the invite link\n**w/google <search>** - Returns an URL for your search\n**w/createinvite *<uses>** - Creates a 24h invite for the server\n**w/wiki <search>** - Returns a Wikipedia page about your query\n**w/ftn <platform> <username>** - Returns your ~~great~~ fortnite stats\n**w/translate <text>** - Translates the text into English".replace("w/", prefix), inline=False)
                generalCommands1.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                generalCommands1.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                generalCommands1.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


                staffCommands = discord.Embed(color=getEmbedColour("default"))
                staffCommands.set_author(name="[2/4]")
                staffCommands.add_field(name="Staff Commands:hammer_pick:", value="**w/clear <number>** - Deletes the given number of messages\n**w/ban <user>** - Bans the user from the discord server\n**w/kick <user>** - Kicks the user from the discord server\n**More commands coming soon**".replace("w/", prefix), inline=False)
                staffCommands.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                staffCommands.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                staffCommands.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


                generalCommands2 = discord.Embed(color=getEmbedColour("default"))
                generalCommands2.set_author(name="[3/4]")
                generalCommands2.add_field(name="Fun Commands:confetti_ball:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Returns a joke\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it'll reply\n**w/diceroll** - Rolls a dice for you\n**w/coinflip** - Flips a coin for you".replace("w/", prefix), inline=False)
                generalCommands2.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                generalCommands2.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                generalCommands2.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


                musicCommands = discord.Embed(color=getEmbedColour("default"))
                musicCommands.set_author(name="[4/4]")
                musicCommands.add_field(name="Music Commands:musical_note:", value="**w/play <song name/title>** - Plays the given song\n**w/pause** - Pauses the song playing\n**w/resume** - Resumes the paused song\n**w/volume <1-100>** - Changes the volume (use numbers from 1-100)\n**w/playing** - Displays the song that playing\n**w/queue** - Returns the current music queue\n**w/skip** - Skips the song playing".replace("w/", prefix), inline=False)
                musicCommands.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                musicCommands.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                musicCommands.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")

                help = await message.channel.send(embed=generalCommands1)

                def check(reac, user):
                    return user == message.author and str(
                        reac.emoji) == "▶" and reac.message.id == help.id or user == message.author and str(
                        reac.emoji) == "◀" and reac.message.id == help.id or user == message.author and str(
                        reac.emoji) == "🇽" and reac.message.id == help.id

                await help.add_reaction(emoji="◀")
                await help.add_reaction(emoji="🇽")
                await help.add_reaction(emoji="▶")
                counter = 0

                for _each in range(0, 30001):
                    try:
                        reac, user = await self.bot.wait_for('reaction_add', check=check, timeout=0.01)
                        if counter <= 0:
                            counter = 0
                            await help.remove_reaction("◀", user)
                        if counter >= 4:
                            counter = 3
                            await help.remove_reaction("▶", user)
                        if "▶" in str(reac.emoji) and user == message.author and "▶" in str(reac.message.reactions):
                            counter += 1
                            if counter == 1:
                                await help.remove_reaction(reac, user)
                                await help.edit(embed=None)
                                await help.edit(embed=staffCommands)
                            elif counter == 2:
                                await help.remove_reaction(reac, user)
                                await help.edit(embed=None)
                                await help.edit(embed=generalCommands2)
                            elif counter == 3:
                                await help.remove_reaction(reac, user)
                                await help.edit(embed=None)
                                await help.edit(embed=musicCommands)
                        elif "◀" in str(reac.emoji) and user == message.author and "◀" in str(reac.message.reactions):
                            counter -= 1
                            if counter == 0:
                                await help.remove_reaction(reac, user)
                                await help.edit(embed=None)
                                await help.edit(embed=generalCommands1)
                            elif counter == 1:
                                await help.remove_reaction(reac, user)
                                await help.edit(embed=None)
                                await help.edit(embed=staffCommands)
                            elif counter == 2:
                                await help.remove_reaction(reac, user)
                                await help.add_reaction("▶")
                                # await option.edit(content="This help message will delete itself in 60 seconds.")
                                await help.edit(embed=None)
                                await help.edit(embed=generalCommands2)  # embed=new_help_emb)
                                # await asyncio.sleep(60)
                                # await old.delete()
                                # break
                                # await option.delete()
                                # await option.delete()
                                # break
                        elif "🇽" in str(reac.emoji):
                            try:
                                await help.delete()
                                await message.delete()
                                break
                            except discord.errors.NotFound:
                                pass
                    except asyncio.TimeoutError:
                        pass


        elif message.guild.me in message.mentions:
            prefix = await self.bot.get_prefix(message)
            prefix = prefix[0]
            embed = discord.Embed(description=f"**Hey {message.author.mention}!**\nCheckout my help command by doing: `{prefix}help`", color=0xE9A72F)
            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))