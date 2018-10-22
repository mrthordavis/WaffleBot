import discord
import asyncio
import random
import traceback


class Events:
    def __init__(self, bot):
        self.bot = bot


    #Need to make an exception on this
    """async def on_guild_channel_create(self, channel):
        if channel.me.guild_permissions.administrator:
            await channel.send("First!")"""


    async def on_guild_join(self, guild):
        embed = discord.Embed(description=f"**{guild} successfully added me**", color=0x15c513)
        embed.set_footer(text=f"I'm currently in {len(self.bot.guilds)} guilds")
        await self.bot.get_channel(458707260978364416).send(embed=embed)


    async def on_guild_remove(self, guild):
        embed = discord.Embed(description=f"**{guild} successfully removed me**", color=0xE73C24)
        embed.set_footer(text=f"I'm currently in {len(self.bot.guilds)} guilds")
        await self.bot.get_channel(458707260978364416).send(embed=embed)


    async def on_member_join(self, member):
        if member.guild.id == 337291099129511937:
            embed = discord.Embed(color=0xE9A72F)
            embed.add_field(name="Welcome to Gamers Hangout!", value=f"Hello {member.mention}! Make sure to check out the <#444489468012003338>")
            owneravi = self.bot.get_user(322449414142558208)
            embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
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
            if member is self.bot:
                embed.add_field(name="Bot", value="True")
            embed.add_field(name="Bot", value="False")
            await self.bot.get_channel(430089438924767253).send(embed=embed)
        else:
            return


    #This is unnecessary and will only flood your logs channel
    async def on_message_edit(self, before, after):
        if after.guild.id == 414493368861589514:
            if after.author.id == 430365624217108484:
                return
            else:
                EditedEmbed = discord.Embed(title="Message Edit", description="**{}** edited a Message In <#{}>.\n**Prior Contents:** `{}`\n**After Contents:** `{}`".format(after.author, after.channel.id, before.content, after.content), colour=0x15c513)
                await self.bot.get_channel(430089438924767253).send(embed=EditedEmbed)
        else:
            return


    async def on_message_delete(self, message):
        if message.guild.id == 414493368861589514:
            if message.author.id == 430365624217108484:
                return
            else:
                embed = discord.Embed(title="Message Deletion", description=f"**{message.author}** deleted a message in <#{message.channel.id}>\n**Content:** `{message.content}`", colour=0x15c513)
                await self.bot.get_channel(430089438924767253).send(embed=embed)


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
            await message.channel.send(f"The current prefix in the guild is: {prefix}")

        #Should be working
        elif message.content.upper() == "W/HELP":
            prefix = await self.bot.get_prefix(message)
            prefix = prefix[0]
            if prefix != "w/":
                embed = discord.Embed(color=0xE9A72F)
                embed.set_author(name="[1/4]")
                embed.add_field(name=":unlock:Info Commands:unlock:", value="**w/roles** - Displays all avaliable roles in the server\n**w/pfp <@name>** - Shows the persons profile picture\n**w/info <@name>** - This command shows you some information about yourself\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Displays how long the bot has been running for\n**w/links** - Sends the support server link and the bot invite link\n**w/google <search>** - Gives you an URL for your search\n**w/createinvite <uses>** - Use this command to create a 24 hour invite to a server\n**w/wiki <search>** - Searches Wikipedia(Keep in mind that this feature might not be able to find your search)\n**w/members** - Shows how many members are in the server\n**w/ftn <platform> <username>** - Retrieves your ~~great~~ fortnite stats".replace("w/", prefix), inline=True)
                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                owneravi = self.bot.get_user(322449414142558208)
                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/422083182167588866/434442848289685505/wafflebot_3.png")

                help = await message.channel.send(embed=embed)

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
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[2/4]")
                                embed.add_field(name=":lock:Staff Commands:lock:", value="**:construction: UNDER CONSTRUCTION :construction:**".replace("w/", prefix), inline=False)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)
                            elif counter == 2:
                                await help.remove_reaction(reac, user)
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[3/4]")
                                embed.add_field(name=":pushpin:General Commands:pushpin:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Tells you a joke\n**w/ping** Pong! :ping_pong:\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it will reply\n**w/diceroll** - The bot will roll a dice for you\n**w/coinflip** - The bot will flip a coin for you".replace("w/", prefix), inline=True)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)
                            elif counter == 3:
                                await help.remove_reaction(reac, user)
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[4/4]")
                                embed.add_field(name=":musical_note:Music commands:musical_note:", value="**w/play <song name/title>** - Plays the given song\n**w/pause & w/resume** - Pauses and resumes the music\n**w/volume <1-100>** - Changes the volume(use numbers from 1-100)\n**w/playing** - Displays the song that is currently being played\n**w/queue** - Shows you what songs are currently in the queue\n**w/skip** - Skips the song currently playing".replace("w/", prefix), inline=True)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)
                        elif "◀" in str(reac.emoji) and user == message.author and "◀" in str(reac.message.reactions):
                            counter -= 1
                            if counter == 0:
                                await help.remove_reaction(reac, user)
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[1/4]")
                                embed.add_field(name=":unlock:Info Commands:unlock:", value="**w/roles** - Displays all avaliable roles in the server\n**w/pfp <@name>** - Shows the persons profile picture\n**w/info <@name>** - This command shows you some information about yourself\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Displays how long the bot has been running for\n**w/links** - Sends the support server link and the bot invite link\n**w/google <search>** - Gives you an URL for your search\n**w/createinvite <uses>** - Use this command to create a 24 hour invite to a server\n**w/wiki <search>** - Searches Wikipedia(Keep in mind that this feature might not be able to find your search)\n**w/members** - Shows how many members are in the server\n**w/ftn <platform> <username>** - Retrieves your ~~great~~ fortnite stats".replace("w/", prefix), inline=True)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/422083182167588866/434442848289685505/wafflebot_3.png")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)
                            elif counter == 1:
                                await help.remove_reaction(reac, user)
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[2/4]")
                                embed.add_field(name=":lock:Staff Commands:lock:", value="**:construction: UNDER CONSTRUCTION :construction:**".replace("w/", prefix), inline=False)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)
                            elif counter == 2:
                                await help.remove_reaction(reac, user)
                                await help.add_reaction("▶")
                                embed = discord.Embed(color=0xE9A72F)
                                embed.set_author(name="[3/4]")
                                embed.add_field(name=":pushpin:General Commands:pushpin:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Tells you a joke\n**w/ping** Pong! :ping_pong:\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it will reply\n**w/diceroll** - The bot will roll a dice for you\n**w/coinflip** - The bot will flip a coin for you".replace("w/", prefix), inline=True)
                                embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                                embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                                owneravi = self.bot.get_user(322449414142558208)
                                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                                # await option.edit(content="This help message will delete itself in 60 seconds.")
                                await help.edit(embed=None)
                                await help.edit(embed=embed)  # embed=new_help_emb)
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
            embed = discord.Embed(description=f"**Hey {message.author.mention}!**\nCheckout my help command by doing: `w/help`", color=0xE9A72F)
            await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))