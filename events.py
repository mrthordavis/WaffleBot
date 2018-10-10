import discord
from discord.ext import commands
import asyncio
import random
import traceback

class Events:
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

    async def on_guild_channel_create(self, channel):
        #Needs testing
        if channel.me.guild_permissions.administrator:
            await channel.send("First!")
        else:
            return

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
            elif message.content.upper() == "!ACCEPT":
                find_role = discord.utils.get(message.guild.roles, id=417057802528358402)
                await message.author.add_roles(find_role)
                embed = discord.Embed(color=0xE9A72F)
                embed.add_field(name="Welcome to WaffleBot Support Server!", value=f"Hello {message.author.mention}! Make sure to check out the <#417743778925903872>")
                owneravi = self.bot.get_user(322449414142558208)
                embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
                await self.bot.get_channel(414493369625214987).send(embed=embed)
                await asyncio.sleep(2)
                await message.delete()
            elif message.content.upper() == "!DECLINE":
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
            
        if message.guild.me in message.mentions:
            embed = discord.Embed(description=f"**Hey {message.author.mention}!**\nCheckout my help command by doing: `w/help`", color=0xE9A72F)
            await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Events(bot))