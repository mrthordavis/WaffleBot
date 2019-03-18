import discord
from discord.ext import commands
import asyncio
import random
import requests #Used for the fortnite command
import json #------||-------
import time #Used for execution time
import wikipedia #Wiki cmd
from googletrans import Translator #Translate command
from pyjokes import get_joke

from utility import getEmbedColour, getEmoji

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(color=0x363941)
        embed.add_field(name="Credits", value="This bot was developed by <@322449414142558208>.\nI would personally like to thank you all the people who helped me with this project: <@170992935951794176>, <@251412743230324736>, <@128819350088974336>, The Labs, Varsity 2.0, Sebi's Bot Tutorial & Discord.py Help Server")
        await ctx.send(embed=embed)


    @commands.command(aliases=["say", "repeat", "s"])
    @commands.is_owner()
    async def echo(self, ctx, *, msg: str = None):
        if msg == None:
            await ctx.send(":x: - You forgot to give me something to say. . .")
        else:
            await ctx.send(msg)


    @commands.command(aliases=["jokes"])
    async def joke(self, ctx):
        await ctx.send(get_joke())


    @commands.command(name="8ball")
    async def _ball(self, ctx, arg = None):
        if arg == None:
            await ctx.send(":x: - You forgot to give me something predict")
        else:
            ball = random.choice(["Yes, I agree", "Nope.", "Hmm, why not", "Well, if you say so", "Most likely", "Not happening", "Never happening", "Not a chance", "Maybe", "Big Shaq is the best mathematician in the world. That's one thing i can agree on", "Can't really give my opinion on that", "No, not imo, but whatever tickles your pickle"])
            await ctx.send(ball)


    @commands.command(aliases=["role", "rolejoin"])
    async def joinrole(self, ctx, role: str = None):
        if ctx.guild.id != 414493368861589514:
            return

        list_of_roles = ["development"]
        dev = discord.utils.get(ctx.message.guild.roles, id=557241924092690433)

        if role is None:
            await ctx.send(f"You can join the following role(s): `development`\nJoin the role by running `w/join <role>`")
        
        if role.lower() in list_of_roles[0]:
            if dev in ctx.author.roles:
                await ctx.author.remove_roles(dev)
                await ctx.send(f"{getEmoji('red_tick')} - You successfully left the WaffleBot Developement role.")
            else:
                await ctx.author.add_roles(dev)
                await ctx.send(f"{getEmoji('green_tick')} - You successfully joined the WaffleBot Development role.")


    @commands.command(aliases=["fortnite", "fort", "fn"])
    @commands.bot_has_permissions(add_reactions=True)
    async def ftn(self, ctx, platform = None,*, player = None):
        if platform is None:
            return await ctx.send(f"{getEmoji('rec_tick')} - Wrong syntax. Correct Syntax: `{ctx.prefix}ftn <platform> <username>`")
        if player is None:
            return await ctx.send(f"{getEmoji('rec_tick')} - Wrong syntax. Correct Syntax: `{ctx.prefix}ftn <platform> <username>`")

        start = time.time()
        msg = await ctx.send("This command can be a bit slow, please be patient :slight_smile:")
        headers = {'TRN-Api-Key': '5d24cc04-926b-4922-b864-8fd68acf482e'}
        r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, player), headers=headers)
        stats = json.loads(r.text)
        stats = stats["stats"]

        # What we want to do here is create a list of three Embeds to send. You're going to treat each section of the JSON response individually.
        # Instead of viewing the error as a whole, we can see each "p" section (p2, p9, etc) as its own response, by setting up three try/except blocks.
        # If one is successful, we move on to the next. Same goes if one fails.
        # At the end, we'll check to see if ALL of them failed, and if so, that account does not exist.
        # This way, as long as one response is valid, the command returns successfully.

        list_of_embeds = []

        end = time.time()
        total = end - start

        # Solos
        try:
            Solo = stats["p2"]
            KDSolo = Solo["kd"]
            KDSolovalue = KDSolo["value"]
            TRNSoloRanking = Solo["trnRating"]
            winsDataSolo = Solo["top1"]
            Soloscore = Solo["score"]
            SoloKills = Solo["kills"]
            SoloMatches = Solo["matches"]
            SoloKPG = Solo["kpg"]
            SoloTop10 = Solo["top10"]
            SoloTop25 = Solo["top25"]

            embed = discord.Embed(colour=getEmbedColour("default"))
            embed.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Solo stats:")
            embed.add_field(name="K/D", value=KDSolovalue)
            embed.add_field(name="Score", value=Soloscore["value"])
            embed.add_field(name="Wins", value=winsDataSolo["value"])
            embed.add_field(name="TRN Rating", value=TRNSoloRanking["value"])
            embed.add_field(name="Kills", value=SoloKills["value"], inline=True)
            embed.add_field(name="Matches Played:", value=SoloMatches["value"], inline=True)
            embed.add_field(name="Kills Per Game:", value=SoloKPG["value"], inline=True)
            embed.add_field(name="Top 10:", value=SoloTop10["value"])
            embed.add_field(name="Top 25:", value=SoloTop25["value"])
            embed.set_footer(text=f"Results returned in {round(total, 2)}s")
            list_of_embeds.append(embed)  # Using the list.append(item) command will add (append) an entry to a list, here a discord.Embed.
        except KeyError:
            pass  # Using a pass expression essentially tells the script "Ignore this and continue as usual".

        # As you can see, if things go well, we have one embed appended to the list. If not, we have none.
        # We'll do this for the next two now.

        # Duos
        try:
            Duo = stats["p10"]
            KDDuo = Duo["kd"]
            KDDuovalue = KDDuo["value"]
            TRNDuoRanking = Duo["trnRating"]
            winsDataDuo = Duo["top1"]
            Duoscore = Duo["score"]
            DuoKills = Duo["kills"]
            DuoMatches = Duo["matches"]
            DuoKPG = Duo["kpg"]
            DuoTop5 = Duo["top5"]
            DuoTop12 = Duo["top12"]

            duo = discord.Embed(color=getEmbedColour("default"))
            duo.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Duo stats:")
            duo.add_field(name="K/D", value=KDDuovalue)
            duo.add_field(name="Score", value=Duoscore["value"])
            duo.add_field(name="Wins", value=winsDataDuo["value"])
            duo.add_field(name="TRN Rating", value=TRNDuoRanking["value"])
            duo.add_field(name="Kills", value=DuoKills["value"], inline=True)
            duo.add_field(name="Matches Played:", value=DuoMatches["value"], inline=True)
            duo.add_field(name="Kills Per Game:", value=DuoKPG["value"], inline=True)
            duo.add_field(name="Top 5:", value=DuoTop5["value"])
            duo.add_field(name="Top 12:", value=DuoTop12["value"])
            duo.set_footer(text=f"Results returned in {round(total, 2)}s")
            list_of_embeds.append(duo)
        except KeyError:
            pass

        # Squads
        try:
            Squad = stats["p9"]
            KDSquad = Squad["kd"]
            KDSquadvalue = KDSquad["value"]
            TRNSquadRanking = Squad["trnRating"]
            winsDataSquad = Squad["top1"]
            Squadscore = Squad["score"]
            SquadKills = Squad["kills"]
            SquadMatches = Squad["matches"]
            SquadKPG = Squad["kpg"]
            SquadTop3 = Squad["top3"]
            SquadTop6 = Squad["top6"]

            squad = discord.Embed(color=getEmbedColour("default"))
            squad.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Squad stats:")
            squad.add_field(name="K/D", value=KDSquadvalue)
            squad.add_field(name="Score", value=Squadscore["value"])
            squad.add_field(name="Wins", value=winsDataSquad["value"])
            squad.add_field(name="TRN Rating", value=TRNSquadRanking["value"])
            squad.add_field(name="Kills", value=SquadKills["value"], inline=True)
            squad.add_field(name="Matches Played:", value=SquadMatches["value"], inline=True)
            squad.add_field(name="Kills Per Game:", value=SquadKPG["value"], inline=True)
            squad.add_field(name="Top 3:", value=SquadTop3["value"])
            squad.add_field(name="Top 6:", value=SquadTop6["value"])
            squad.set_footer(text=f"Results returned in {round(total, 2)}s")
            list_of_embeds.append(squad)
        except KeyError:
            pass

        # Now that we've gone through all three sections, we need to make sure that there is at least one embed that did not fail.
        # Basically, we need to make sure that the list of embeds is not empty.
    
        if not list_of_embeds:  # For whatever reason, Python treats empty arrays as False literals. Use it to your advantage!
            await msg.delete()
            await ctx.send(f"{getEmoji('red_tick')} - Wrong username, please try again with a valid username")

            
        send = await ctx.send(embed=embed)
        await msg.delete()

        def check(reac, user):
            return user == ctx.author and str(
                reac.emoji) == "▶" and reac.message.id == send.id or user == ctx.author and str(
                reac.emoji) == "◀" and reac.message.id == send.id or user == ctx.author and str(
                reac.emoji) == "🇽" and reac.message.id == send.id

        await send.add_reaction(emoji="◀")
        await send.add_reaction(emoji="🇽")
        await send.add_reaction(emoji="▶")
        counter = 0
        for _each in range(0, 30001):
            try:
                reac, user = await self.bot.wait_for('reaction_add', check=check, timeout=0.01)
                if counter <= 0:
                    counter = 0
                    await send.remove_reaction("◀", user)
                if counter >= 4:
                    counter = 3
                    await send.remove_reaction("▶", user)
                if "▶" in str(reac.emoji) and user == ctx.author and "▶" in str(reac.message.reactions):
                    counter += 1
                    if counter == 1:
                        await send.remove_reaction(reac, user)
                        #await send.edit(embed=None)
                        await send.edit(embed=duo)
                    if counter == 2:
                        await send.remove_reaction(reac, user)
                        #await send.edit(embed=None)
                        await send.edit(embed=squad)
                elif "◀" in str(reac.emoji) and user == ctx.author and "◀" in str(reac.message.reactions):
                    counter -= 1
                    if counter == 0:
                        await send.remove_reaction(reac, user)
                        #await send.edit(embed=None)
                        await send.edit(embed=embed)
                    if counter == 1:
                        await send.remove_reaction(reac, user)
                        #await send.edit(embed=None)
                        await send.edit(embed=duo)
                    if counter == 2:
                        await send.remove_reaciton(reac, user)
                        await send.add_reaction("▶")
                        #await send.edit(embed=None)
                        await send.edit(embed=squad)
                elif "🇽" in str(reac.emoji):
                    try:
                        await send.delete()
                        await ctx.message.delete()
                        break
                    except discord.errors.NotFound:
                        pass
            except asyncio.TimeoutError:
                pass


    @commands.command(aliases=["ui", "userinfo", "user"])
    async def info(self, ctx, user: discord.Member = None):
        if user == None:
            none = discord.Embed(color=getEmbedColour("default"))
            none.set_author(icon_url=ctx.message.author.avatar_url, name="Here's some info about {}".format(ctx.message.author.name))
            none.set_thumbnail(url=ctx.message.author.avatar_url)
            none.add_field(name="Name:", value=ctx.message.author.name, inline=True)
            roles = 0
            for ctx.role in ctx.message.author.roles:
                roles += 1
            none.add_field(name="User Roles:", value=roles, inline=True)
            none.add_field(name="Users ID:", value=ctx.message.author.id, inline=True)
            none.add_field(name="Users Highest role:", value=ctx.message.author.top_role.mention, inline=True)
            none.add_field(name="Discriminator:", value=f"#{ctx.message.author.discriminator}", inline=True)
            if ctx.message.author.activity is None:
                none.add_field(name="Playing:", value="Not playing :thinking:")
            else:
                none.add_field(name="Playing:", value=ctx.message.author.activity.name, inline=True)
            none.add_field(name="Joined:", value=str(ctx.message.author.joined_at)[:19], inline=True)
            none.add_field(name="Account Creation:", value=str(ctx.message.author.created_at)[:19], inline=True)
            await ctx.send(embed=none)
        else:
            embed = discord.Embed(color=getEmbedColour("default"))
            embed.set_author(icon_url=user.avatar_url, name="Here's some info about {}".format(user.name))
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="Name:", value=user.name, inline=True)
            roles = 0
            for ctx.role in user.roles:
                roles += 1
            embed.add_field(name="User roles:", value=roles, inline=True)
            embed.add_field(name="Users ID:", value=user.id, inline=True)
            embed.add_field(name="Users Highest role:", value=user.top_role.mention, inline=True)
            embed.add_field(name="Discriminator:", value=f"#{user.discriminator}", inline=True)
            if user.activity is None:
                embed.add_field(name="Playing:", value="Not Playing")
            else:
                embed.add_field(name="Playing:", value=user.activity.name, inline=True)
            embed.add_field(name="Joined:", value=str(user.joined_at)[:19], inline=True)
            embed.add_field(name="Account Creation:", value=str(user.created_at)[:19], inline=True)
            await ctx.send(embed=embed)


    @commands.command(aliases=["invite", "link"])
    async def links(self, ctx):
        embed = discord.Embed(color=getEmbedColour("default"))
        embed.add_field(name="Links", value="[Offical Server!](https://discord.gg/6M83Wvz)\n[Add Me!](https://discordapp.com/api/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        owneravi = self.bot.get_user(322449414142558208)
        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
        await ctx.send(embed=embed)


    @commands.command(aliass=["createserverinvite", "serverinvite"])
    async def createinvite(self, ctx, uses: int = None):
        if uses == None:
            invitechannel = await ctx.channel.create_invite(max_uses=0, max_age=60*60*24, unique=False)
            await ctx.send(f"Here is your channel invite: {invitechannel}\n**The invite is only valid for 24 hours**")
        else:
            invitechannele = await ctx.channel.create_invite(max_uses=uses, max_age=60*60*24, unique=False)
            await ctx.send(f"Here is your channel invite which can be used {uses} times: {invitechannele}\n**The invite is only valid for 24 hours**")


    @commands.command(aliases=["si", "serverinformation", "member", "membercount", "members"])
    async def serverinfo(self, ctx):
        embed = discord.Embed(color=getEmbedColour("default"))
        embed.set_author(icon_url=ctx.message.guild.icon_url, name="{}'s info".format(ctx.message.guild.name))
        embed.add_field(name="Name:", value=ctx.message.guild.name, inline=True)
        embed.add_field(name="ID:", value=ctx.message.guild.id, inline=True)
        embed.add_field(name="Region:", value=ctx.message.guild.region, inline=True)
        embed.add_field(name="Members:", value=len(ctx.message.guild.members), inline=True)
        bot_count = sum(m.bot for m in ctx.guild.members)
        human_count = len(ctx.message.guild.members) - bot_count
        embed.add_field(name="Humans:", value=human_count, inline=True)
        embed.add_field(name="Bots:", value=bot_count, inline=True)
        embed.add_field(name="Roles:", value=len(ctx.message.guild.roles), inline=True)
        embed.add_field(name="Text channels:", value=len(ctx.guild.text_channels))
        embed.add_field(name="Categories", value=len(ctx.guild.categories))
        embed.add_field(name="Owner ID:", value=ctx.guild.owner.id)
        embed.add_field(name="Server Created At:", value=str(ctx.guild.created_at)[:19], inline=True)
        embed.add_field(name="Owner:", value=ctx.message.guild.owner, inline=True)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.set_footer(icon_url=ctx.message.guild.icon_url, text=f"{ctx.message.guild.name} | By: {ctx.guild.owner.name}#{ctx.guild.owner.discriminator}")
        await ctx.send(embed=embed)


    @commands.command(aliases=["lookup"])
    async def google(self, ctx, *, googlesearch: str = None):
        if googlesearch == None:
            await ctx.send(f"{getEmoji('red_tick')} - You didn't give me anything to google *smh*")
        else:
            string = f"https://www.google.com/search?q={googlesearch}"
            await ctx.send(string.replace(" ", "+"))


    @commands.command(aliases=["serverroles"])
    async def roles(self, ctx):
        role_mentions = str([role.mention for role in ctx.message.guild.roles]).replace("[", "").replace("]", "").replace("'", "").replace(f"{ctx.message.guild.default_role.mention}, ", "@everyone, ")
        embed = discord.Embed(color=getEmbedColour("default"))
        embed.set_author(icon_url=ctx.message.guild.icon_url, name="List of roles in {}".format(ctx.message.guild.name))
        embed.add_field(name="Roles:", value=role_mentions, inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=["profilepicture", "avatar"])
    async def pfp(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(title="Profile Picture of {}".format(ctx.message.author.name), color=getEmbedColour("default"))
            emb.set_image(url=ctx.message.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            embed = discord.Embed(title="Profile Picture of {}".format(user.name), color=getEmbedColour("default"))
            embed.set_image(url=user.avatar_url)
            await ctx.send(embed=embed)
    

    @commands.command(aliases=["coin", "flipacoin"])
    async def coinflip(self, ctx):
        flip = random.choice(["The coin landed on __heads__💰", "The coin landed on __tails__💰"])
        await ctx.send(f"{flip}")


    @commands.command(aliases=["trans"])
    async def translate(self, ctx, *, text: str = None):
        translator = Translator()
        if text == None:
            await ctx.send("<:redtick:506537775642968095> - You didn't give me a string to translate")
        else:
            await ctx.send(f"**Translated text:** {translator.translate(text, dest='en').text}\n**Language:** {translator.detect(text).lang}\n`{text} -> {translator.translate(text, dest='en').text}`")


    @commands.command(aliases=["pong", "latency"])
    async def ping(self, ctx):
        start = time.time()

        await ctx.message.channel.trigger_typing()

        end = (time.time() - start) * 1000

        await ctx.send(f"Ping: `{(str(int(round(end, 0))))}ms` :ping_pong:\nApi Latency: `{(round(self.bot.latency*1000))}ms`")
    

    @commands.command(aliases=["waffle", "gif"])
    async def wafflegif(self, ctx):
        gif = random.choice(["https://i.imgur.com/ZYtYt5O.gif", "https://i.imgur.com/hffKEIn.gif", "https://i.imgur.com/x9mg3Sj.gif", "https://i.imgur.com/0zlVS7w.gif", "https://i.imgur.com/ez4ZsMS.gif", "https://i.imgur.com/87Sl6.gif", "https://i.imgur.com/UnKylQk.gif", "https://i.imgur.com/S0MekgX.gif", "https://i.imgur.com/KieFRUb.gif", "https://i.imgur.com/3YrdkCz.gif", "https://i.imgur.com/8pbG99c.gif"])
        embed= discord.Embed(color=getEmbedColour("default"))
        embed.set_image(url=f"{gif}")
        owneravi = self.bot.get_user(322449414142558208)
        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
        await ctx.send(embed=embed)


    #Needs rewriting, currently it's way longer than it needs to be.
    @commands.command(aliases=["rockpaperscissors", "rock", "paper", "scissors"])
    async def rps(self, ctx, choice = None):
        if choice == None:
            return await ctx.send(f"{getEmoji('red_tick')} - You forgot to pick 1 of the 3 choices (rock, paper, scissors)")
        rps = random.choice(["Rock", "Paper", "Scissors"])
        if choice.upper() == "PAPER":
            if rps == "Rock":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="**Paper** beats **rock**, which means you win!", color=0x15c513)
                await ctx.send(embed=embed)
            if rps == "Scissors":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="**Scissors** beat **paper**, which means I win!", color=0xE73C24)
                await ctx.send(embed=embed)
            if rps == "Paper":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="It's a tie, which means no one wins!", color=0xE9A72F)
                await ctx.send(embed=embed)
        if choice.upper() == "ROCK":
            if rps == "Rock":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="It's a tie, which means no one wins!", color=0xE9A72F)
                await ctx.send(embed=embed)
            if rps == "Scissors":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="**Rock** beats **scissors**, which means you win!", color=0x15c513)
                await ctx.send(embed=embed)
            if rps == "Paper":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="**Paper** beats **rock**, which means I win!", color=0xE73C24)
                await ctx.send(embed=embed)
        if choice.upper() == "SCISSORS":
            if rps == "Rock":
                embed = discord.Embed(title=f"You chose Scissors, I chose {rps}", description="**Rock** beats **scissors**, which means I win!", color=0xE73C24)
                await ctx.send(embed=embed)
            if rps == "Scissors":
                embed = discord.Embed(title=f"You chose Scissors, I chose {rps}", description="It's a tie, which means no one wins!", color=0xE9A72F)
                await ctx.send(embed=embed)
            if rps == "Paper":
                embed = discord.Embed(title=f"You chose Scissors, I chose {rps}", description="**Scissors** beat **paper**, which means you win!", color=0x15c513)
                await ctx.send(embed=embed)


    @commands.command(aliases=["wikipedia", "search", "libary", "wikisearch"])
    async def wiki(self, ctx, *, search: str = None):
        if search is None:
            await ctx.send(f"{getEmoji('red_tick')} - You forgot to give me a search")
        else:
            print("I'm called!")
            query = search
            while len(query) != 0 and query[0] == " ":
                query = query.lstrip()
            (lang, query) = await self.setlang(query)
            print("Query = " + query)
            await self.printout(ctx, query, lang)

    async def printout(self, ctx, query, lang):
        wikipage = None
        lookup = True
        disambiguation = False
        wikipedia.set_lang(lang)
        try:
            wikipage = wikipedia.page(query)
        except wikipedia.PageError:
            await ctx.send(f"{getEmoji('red_tick')} - I can't access this page, please try with something else")
        except wikipedia.DisambiguationError:
            await ctx.send(f"{getEmoji('red_tick')} - This search leads to a disambiguation page. Please be more specific")
            disambiguation = True
        except Exception:
            lookup = False
        if wikipage is None and lookup and not disambiguation:
            wikipage = wikipedia.suggest(query)
        if wikipage is None and lookup and not disambiguation:
            await ctx.send(f"{getEmoji('red_tick')} - Sorry, I cannot find {query}")
        elif not lookup:
            emb = discord.Embed(title="Error:", description="Something went wrong. Check the language, or maybe I can't reach Wikipedia")
            await ctx.send(embed=emb)
        else:
            imglist = wikipage.images
            if len(imglist) == 0:
                em = discord.Embed(title=wikipage.title, description=wikipedia.summary(query, sentences=2), colour=getEmbedColour("default"), url=wikipage.url)
            else:
                em = discord.Embed(title=wikipage.title, description=wikipedia.summary(query, sentences=2), colour=getEmbedColour("default"), url=wikipage.url, image=imglist[0])
                em.set_footer(icon_url=ctx.message.author.avatar_url, text=f"Article Requested By: {ctx.message.author.name}#{ctx.message.author.discriminator}")
                await ctx.send(embed=em)
                await ctx.send("More at <" + wikipage.url + ">")

        wikipedia.set_lang("en")

    async def setlang(self, query):
        if len(query) <= 4 or query[0] != '!' or query[3] != " ":
            return "en", query
        else:
            lang = query[1] + query[2]
            nquery = query[4:]
            return lang, nquery


def setup(bot):
    bot.add_cog(GeneralCommands(bot))