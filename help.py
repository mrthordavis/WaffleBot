import discord
from discord.ext import commands
import asyncio
#from main import bot_prefix

class Help:
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.command()
    async def help(self, ctx):
        
        embed = discord.Embed(color=0xE9A72F)
        embed.add_field(name=":unlock:Info Commands:unlock:", value="**w/roles** - Displays all avaliable roles in the server\n**w/pfp <@name>** - Shows the persons profile picture\n**w/info <@name>** - This command shows you some information about yourself\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Displays how long the bot has been running for\n**w/links** - Sends the support server link and the bot invite link\n**w/google <search>** - Gives you an URL for your search\n**w/createinvite <uses>** - Use this command to create a 24 hour invite to a server\n**w/wiki <search>** - Searches Wikipedia(Keep in mind that this feature might not be able to find your search)\n**w/members** - Shows how many members are in the server\n**w/ftn <platform> <username>** - Retrieves your ~~great~~ fortnite stats", inline=True)
        embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
        owneravi = self.bot.get_user(322449414142558208)
        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/422083182167588866/434442848289685505/wafflebot_3.png")

        help = await ctx.send(embed=embed)

        def check(reac, user):
            return user == ctx.author and str(
                reac.emoji) == "▶" and reac.message.id == help.id or user == ctx.author and str(
                reac.emoji) == "◀" and reac.message.id == help.id or user == ctx.author and str(
                reac.emoji) == "🇽" and reac.message.id == help.id

        await help.add_reaction(emoji="◀")
        await help.add_reaction(emoji="🇽")
        await help.add_reaction(emoji="▶")
        counter = 0
        for each in range(0, 30001):
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
                        embed = discord.Embed(color=0xE9A72F)
                        embed.add_field(name=":lock:Staff Commands:lock:", value="**w/setprefix <new prefix>** - Changes the current prefix of the bot\n**w/delete <x>** - Deletes x number of messages\n**w/kick <@name>** - Kicks the specified user\n**w/nick <@name> <new nickname>** - Changes the users nickname\n**w/warn <@name>** - Warns the user mentioned\n**w/clearwarns <@name>** - Clears a users previous warns\n**w/mute <@name>** - Mutes the tagged user\n**w/unmute <@name>** - Pretty self-explanatory\n**w/ban <@name>** - Bans the person mentioned")
                        embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                        embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                        owneravi = self.bot.get_user(322449414142558208)
                        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                        await help.edit(embed=None)
                        await help.edit(embed=embed)
                    elif counter == 2:
                        await help.remove_reaction(reac, user)
                        embed = discord.Embed(color=0xE9A72F)
                        embed.add_field(name=":pushpin:General Commands:pushpin:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Tells you a joke\n**w/ping** Pong! :ping_pong:\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it will reply\n**w/diceroll** - The bot will roll a dice for you\n**w/coinflip** - The bot will flip a coin for you", inline=True)
                        embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                        embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                        owneravi = self.bot.get_user(322449414142558208)
                        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                        await help.edit(embed=None)
                        await help.edit(embed=embed)
                    elif counter == 3:
                        await help.remove_reaction(reac, user)
                        embed = discord.Embed(color=0xE9A72F)
                        embed.add_field(name=":musical_note:Music commands:musical_note:", value="**w/play <song name/title>** - Plays the given song\n**w/pause & w/resume** - Pauses and resumes the music\n**w/volume <1-100>** - Changes the volume(use numbers from 1-100)\n**w/playing** - Displays the song that is currently being played\n**w/queue** - Shows you what songs are currently in the queue\n**w/skip** - Skips the song currently playing", inline=True)
                        embed.add_field(name=":incoming_envelope:Invite me to your server:incoming_envelope:", value="[Click Here!](https://discordapp.com/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
                        embed.add_field(name=":paperclip:Help Server:paperclip:", value="[Join here!](https://discord.gg/6M83Wvz)", inline=True)
                        owneravi = self.bot.get_user(322449414142558208)
                        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                        await help.edit(embed=None)
                        await help.edit(embed=embed)
                elif "◀" in str(reac.emoji) and user == ctx.author and "◀" in str(reac.message.reactions):
                    counter -= 1
                    if counter == 0:
                        await help.remove_reaction(reac, user)
                        embed = discord.Embed(color=0xE9A72F)
                        embed.add_field(name=":unlock:Info Commands:unlock:", value="**w/roles** - Displays all avaliable roles in the server\n**w/pfp <@name>** - Shows the persons profile picture\n**w/info <@name>** - This command shows you some information about yourself\n**w/serverinfo** - Displays some information about the server\n**w/uptime** - Displays how long the bot has been running for\n**w/links** - Sends the support server link and the bot invite link\n**w/google <search>** - Gives you an URL for your search\n**w/createinvite <uses>** - Use this command to create a 24 hour invite to a server\n**w/wiki <search>** - Searches Wikipedia(Keep in mind that this feature might not be able to find your search)\n**w/members** - Shows how many members are in the server\n**w/ftn <platform> <username>** - Retrieves your ~~great~~ fortnite stats", inline=True)
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
                        embed.add_field(name=":lock:Staff Commands:lock:", value="**w/setprefix <new prefix>** - Changes the current prefix of the bot\n**w/delete <x>** - Deletes x number of messages\n**w/kick <@name>** - Kicks the specified user\n**w/nick <@name> <new nickname>** - Changes the users nickname\n**w/warn <@name>** - Warns the user mentioned\n**w/clearwarns <@name>** - Clears a users previous warns\n**w/mute <@name>** - Mutes the tagged user\n**w/unmute <@name>** - Pretty self-explanatory\n**w/ban <@name>** - Bans the person mentioned")
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
                        embed.add_field(name=":pushpin:General Commands:pushpin:", value="**w/wafflegif** - Sends a 'wafflegif'\n**w/joke** - Tells you a joke\n**w/ping** Pong! :ping_pong:\n**w/rps <choice>** - Play rock, paper, scissors against the bot\n**w/8ball** - Ask the mysterious 8Ball anything and it will reply\n**w/diceroll** - The bot will roll a dice for you\n**w/coinflip** - The bot will flip a coin for you", inline=True)
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
                        await ctx.message.delete()
                        break
                    except discord.errors.NotFound:
                        pass
            except asyncio.TimeoutError:
                pass
                
def setup(bot):
    bot.add_cog(Help(bot))