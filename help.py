import discord
from discord.ext import commands
import asyncio

from utility import getEmbedColour

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.command(aliases=["commands"])
    @commands.bot_has_permissions(add_reactions=True)
    async def help(self, ctx):

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
        generalCommands1.add_field(name="General Commands:pushpin:", value="**w/ping** Pong! :ping_pong:\n**w/roles** - Lists all roles in the sever\n**w/setprefix <new prefix>** - Changes the default prefix\n**w/info *<user>** - Shows some information about you\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Shows the bots current uptime\n**w/links** - Get the support server and the invite link\n**w/google <search>** - Returns an URL for your search\n**w/createinvite *<uses>** - Creates a 24h invite for the server\n**w/wiki <search>** - Returns a Wikipedia page about your query\n**w/ftn <platform> <username>** - Returns your ~~great~~ fortnite stats\n**w/translate <text>** - Translates the text into English".replace("w/", ctx.prefix), inline=False)
        generalCommands1.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        generalCommands1.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
        owneravi = self.bot.get_user(322449414142558208)
        generalCommands1.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


        staffCommands = discord.Embed(color=getEmbedColour("default"))
        staffCommands.set_author(name="[2/4]")
        staffCommands.add_field(name="Staff Commands:hammer_pick:", value="**w/clear <number>** - Deletes the given number of messages\n**w/ban <user>** - Bans the user from the discord server\n**w/kick <user>** - Kicks the user from the discord server\n**More commands coming soon**".replace("w/", ctx.prefix), inline=False)
        staffCommands.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        staffCommands.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
        owneravi = self.bot.get_user(322449414142558208)
        staffCommands.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


        generalCommands2 = discord.Embed(color=getEmbedColour("default"))
        generalCommands2.set_author(name="[3/4]")
        generalCommands2.add_field(name="Fun Commands:confetti_ball:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Returns a joke\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it'll reply\n**w/diceroll** - Rolls a dice for you\n**w/coinflip** - Flips a coin for you".replace("w/", ctx.prefix), inline=False)
        generalCommands2.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        generalCommands2.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
        owneravi = self.bot.get_user(322449414142558208)
        generalCommands2.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")


        musicCommands = discord.Embed(color=getEmbedColour("default"))
        musicCommands.set_author(name="[4/4]")
        musicCommands.add_field(name="Music Commands:musical_note:", value="**w/play <song name/title>** - Plays the given song\n**w/pause** - Pauses the song playing\n**w/resume** - Resumes the paused song\n**w/volume <1-100>** - Changes the volume (use numbers from 1-100)\n**w/playing** - Displays the song that playing\n**w/queue** - Returns the current music queue\n**w/skip** - Skips the song playing".replace("w/", ctx.prefix), inline=False)
        musicCommands.add_field(name="Invite me:link:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        musicCommands.add_field(name="Help Server:blue_book:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
        owneravi = self.bot.get_user(322449414142558208)
        musicCommands.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960 || All arguments with a * are optional")

        help = await ctx.send(embed=generalCommands1)

        def check(reac, user):
            return user == ctx.author and str(
                reac.emoji) == "▶" and reac.message.id == help.id or user == ctx.author and str(
                reac.emoji) == "◀" and reac.message.id == help.id or user == ctx.author and str(
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
                if "▶" in str(reac.emoji) and user == ctx.author and "▶" in str(reac.message.reactions):
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
                elif "◀" in str(reac.emoji) and user == ctx.author and "◀" in str(reac.message.reactions):
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
                        await ctx.message.delete()
                        break
                    except discord.errors.NotFound:
                        pass
            except asyncio.TimeoutError:
                pass


def setup(bot):
    bot.add_cog(Help(bot))