import discord
from discord.ext import commands
import asyncio
import random

class Events():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if ctx.cog == '':
            return
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(color=0xE73C24)
            embed.add_field(name="Houston, we have a problem:", value="I couldn't find the command you were looking for, try **w/help**")
            await ctx.send(embed=embed)
            print(error)
            await ctx.message.add_reaction(emoji="❓")
        elif error.__cause__.__class__.__name__ == 'Forbidden':
            embedd = discord.Embed(title="Error:", description="Looks like I don't have the right perms to execute this command, please make sure I have the perms needed", color=0xE73C24)
            await ctx.send(embed=embedd)
        elif isinstance(error, commands.MissingPermissions):
            error = discord.Embed(color=0xE73C24)
            error.add_field(name="Error:", value="You don't have permission to do that!")
            await ctx.send(embed=error)
            print(error)
        elif isinstance(error, commands.NotOwner):
            await ctx.send("**You do not own this bot**")
        else:
            print(error)

    async def on_guild_channel_create(self, channel):
        await channel.send("First!")
        
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
        else:
            return

    async def on_message(self, message):
        #WaffleBot Server
        if message.channel.name == "rules":
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
        
        #The Labs
        elif message.channel.name == "gate":
            if message.content.upper() != "!ACCEPT" and message.content.upper() != "!DECLINE":
                await message.delete()
            elif message.content.upper() == "!ACCEPT":
                noob = discord.utils.get(message.guild.roles, id=449600245031108608)
                registered = discord.utils.get(message.guild.roles, id=449600245047754774)
                await message.author.add_roles(noob, registered)
                embed = discord.Embed(color=0xE9A72F)
                channel = self.bot.get_channel(449606135129833476)
                em = discord.Embed(title="User Registered", description=f"{message.author.name} succesfully registered!", colour=0x55FF55)
                em.set_footer(text="We now have %s members!" % (len(message.guild.members)))
                await channel.send(embed=em)
                await asyncio.sleep(2)
                await message.delete()

        #The Labs lock
        elif message.content.upper().startswith("!LOCK"):
            if "Staff" in [role.name for role in message.author.roles]:
                await message.delete()
                default = discord.utils.get(message.guild.roles, name="Registered")
                perms = default.permissions
                perms.send_messages = False
                try:
                    time = int(message.content.split()[1]) * 60 #time in minutes (seconds -> minutes)
                except IndexError: #Saves us having to check the len() of the args, also means we don't have to make redundent code here 
                    time = 0
                await default.edit(permissions=perms)
                if time == 0: #Basically if it = 0 then the lock is perm until someoone !unlock's it
                    nEmbed = discord.Embed(title="Server Locked", description="The server has been locked by %s" % (message.author.mention), colour=0xFF5555)
                else:
                    nEmbed = discord.Embed(title="Server Locked", description="The server has been locked by %s for **%s minutes**" % (message.author.mention, str(time/60)), colour=0xFF5555)
                nEmbed.set_footer(text="This bot is not capable of enforcing Discord Terms of Service but may submit statistical data to Trust & Safety using data collected by Guardian")
                logChannel = self.bot.get_channel(449614348122587136)
                notice = await message.channel.send(embed=nEmbed)
                await logChannel.send(embed=nEmbed)
                if not time == 0:
                    await asyncio.sleep(time)
                    perms.send_messages = True
                    await default.edit(permissions=perms)
                    await notice.delete()

        #The Labs lock
        elif message.content.upper().startswith("!UNLOCK"):
            if "Staff" in [role.name for role in message.author.roles]:
                await message.delete()
                default = discord.utils.get(message.guild.roles, name="Registered")
                perms = default.permissions
                perms.send_messages = True
                await default.edit(permissions=perms)
                nEmbed = discord.Embed(title="Server Unlocked", description="The server has been unlocked by %s" % (message.author.mention), colour=0x55FF55)
                nEmbed.set_footer(text="This bot is not capable of enforcing Discord Terms of Service but may submit statistical data to Trust & Safety using data collected by Guardian")
                logChannel = self.bot.get_channel(449614348122587136)
                notice = await message.channel.send(embed=nEmbed)
                await logChannel.send(embed=nEmbed)

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

        elif message.content.upper().startswith("DAB"):
            if message.author.id == 322449414142558208:
                pass
            else:
                await message.delete()
                await message.channel.send("**No Dabbing Allowed <o/**")
            
        if message.guild.me in message.mentions:
            embed = discord.Embed(description=f"**Hey {message.author.mention}!** Checkout my help command by doing: `w/help`", color=0xE9A72F)
            await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Events(bot))