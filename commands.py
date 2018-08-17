import discord
from discord.ext import commands
import asyncio
import random
import datetime
import requests
import json
import time
import wikipedia

class GeneralCommands():
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

    @commands.command(aliases=["reaction"])
    async def react(self, ctx):
        await ctx.message.add_reaction(emoji="👍🏼")
        await ctx.message.add_reaction(emoji="👎🏼")
    
    @commands.command(aliases=["jokes"])
    async def joke(self, ctx):
        joke = random.choice(["What do you call a bee that can’t make up its mind?\nA Maybe", "What do you call a pig that does karate?\nPork chop", "I’m only friends with 25 letters of the alphabet.\nI don’t know Y.", "Why did the computer show up late to work?\nIt had a hard drive", "Autocorrect has become my worst enema.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Don’t you hate it when someone answers their own questions?\nI do.", "If I got 50 cents for every failed math exam, I’d have $ 6.30 now.", "I wrote a song about a tortilla. Well actually, it’s more of a wrap.", "My girlfriend and I often laugh about how competitive we are. But I laugh more", "You", "Your wifi", "Do you think I'm a bad mom Peter?\nMy name is Paul", "Why can't a blonde dial 911?\nShe can't find eleven", "What do you call a belt made of watches?\nA waist of time"])
        await ctx.send(joke)

    @commands.command(name="8ball")
    async def _ball(self, ctx):
        ball = random.choice(["Yes, I agree", "Nope.", "Hmm, why not", "Well, if you say so", "Most likely", "Not happening", "Never happening", "Not a chance", "Maybe", "Big Shaq is the best mathematician in the world. That's one thing i can agree on", "Can't really give my opinion on that", "No, not imo, but whatever tickles your pickle"])
        await ctx.send(ball)

    @commands.command(aliases=["fortnite", "fort", "fn"])
    async def ftn(self, ctx, platform = None,*, player = None):
        if platform is None:
            el = discord.Embed(title="Error:", description="You didn't specify a platform: w/ftn <platform> <username>", color=0xE73C24)
            return await ctx.send(embed=el)  # Adding return here ends the script from executing further within the func.
        if player is None:
            ell = discord.Embed(title="Error:", description="You didn't specify a username: w/ftn <platform> <username>", color=0xE73C24)
            return await ctx.send(embed=ell)

        msg = await ctx.send("This command can be very slow, please be patient :slight_smile:")
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

            embed = discord.Embed(colour=0xE9A72F)
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

            duo = discord.Embed(color=0xE9A72F)
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

            squad = discord.Embed(color=0xE9A72F)
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
            list_of_embeds.append(squad)
        except KeyError:
            pass

        # Now that we've gone through all three sections, we need to make sure that there is at least one embed that did not fail.
        # Basically, we need to make sure that the list of embeds is not empty.
    
        if not list_of_embeds:  # For whatever reason, Python treats empty arrays as False literals. Use it to your advantage!
            await msg.delete()
            error = discord.Embed(color=0xE73C24)
            error.add_field(name="Error:", value="Invalid username, please try again with another name")
            await ctx.send(embed=error)
            print(error)
        #else:
            #If the embed list if not empty, we'll create a for loop and send each.
            #await msg.delete()
            #for embed in list_of_embeds:
                #await ctx.send(embed=embed)
        else:
            
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
            for each in range(0, 30001):
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

    @commands.command(aliases=["ui", "userinfo"])
    async def info(self, ctx, user: discord.Member = None):
        if user == None:
            none = discord.Embed(color=0xE9A72F)
            none.set_author(icon_url=ctx.message.author.avatar_url, name="Here's some info about {}".format(ctx.message.author.name))
            none.set_thumbnail(url=ctx.message.author.avatar_url)
            none.add_field(name="Name:", value=ctx.message.author.name, inline=True)
            none.add_field(name="Status:", value=ctx.message.author.status, inline=True)
            none.add_field(name="Users ID:", value=ctx.message.author.id, inline=True)
            none.add_field(name="Users Highest role:", value=ctx.message.author.top_role.mention, inline=True)
            none.add_field(name="Discriminator:", value=f"#{ctx.message.author.discriminator}", inline=True)
            if ctx.message.author.activity == None:
                none.add_field(name="Playing:", value="Not playing :thinking:")
            else:
                none.add_field(name="Playing:", value=ctx.message.author.activity.name, inline=True)
            none.add_field(name="Joined", value=str(ctx.message.author.joined_at)[:19], inline=True)
            none.add_field(name="Account Creation:", value=str(ctx.message.author.created_at)[:19], inline=True)
            await ctx.send(embed=none)
        else:
            embed = discord.Embed(color=0xE9A72F)
            embed.set_author(icon_url=user.avatar_url, name="Here's some info about {}".format(user.name))
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="Name:", value=user.name, inline=True)
            embed.add_field(name="Status:", value=user.status, inline=True)
            embed.add_field(name="Users ID:", value=user.id, inline=True)
            embed.add_field(name="Users Highest role:", value=user.top_role.mention, inline=True)
            embed.add_field(name="Discriminator:", value=f"#{user.discriminator}", inline=True)
            if user.activity == None:
                embed.add_field(name="Playing:", value="Not Playing")
            else:
                embed.add_field(name="Playing:", value=user.activity.name, inline=True)
            embed.add_field(name="Joined", value=str(user.joined_at)[:19], inline=True)
            embed.add_field(name="Account Creation:", value=str(user.created_at)[:19], inline=True)
            await ctx.send(embed=embed)

    @commands.command(aliases=["invite", "link"])
    async def links(self, ctx):
        embed = discord.Embed(color=0x363941)
        embed.add_field(name="Links", value="[Offical Server!](https://discord.gg/6M83Wvz)\n[Add Me!](https://discordapp.com/api/oauth2/authorize?client_id=430365624217108484&permissions=8&scope=bot)")
        owneravi = self.bot.get_user(322449414142558208)
        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
        await ctx.send(embed=embed)

    @commands.command(aliass=["createserverinvite", "serverinvite"])
    async def createinvite(self, ctx, uses: int = None):
        if uses == None:
            invitechannel = await ctx.channel.create_invite(max_uses=0, max_age=60*60*24, unique=False)
            await ctx.send(f"Here is your channel invite: {invitechannel}\n**This invite is only valid for 24 hours**")
        else:
            invitechannele = await ctx.channel.create_invite(max_uses=uses, max_age=60*60*24, unique=False)
            await ctx.send(f"Here is your channel invite which can be used {uses} times: {invitechannele}\n**This invite is only valid for 24 hours**")

    @commands.command(aliases=["bi"])
    async def botinfo(self, ctx):
        embed = discord.Embed(color=0xE9A72F)
        embed.add_field(name="Guilds:", value=len(ctx.bot.guilds))
        embed.add_field(name="Members:", value=len(ctx.bot.users), inline=False)
        embed.add_field(name="Creator:", value="<@322449414142558208>", inline=False)
        embed.add_field(name="Libary:", value="Discord.py")
        await ctx.send(embed=embed)

    @commands.command(aliases=["si", "serverinformation", "member", "membercount", "members"])
    async def serverinfo(self, ctx):
        embed = discord.Embed(color=0xE9A72F)
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
            await ctx.send(":x: - You didn't give me anything to google *smh*")
        else:
            string = f"https://www.google.com/search?q={googlesearch}"
            await ctx.send(string.replace(" ", "+"))

    @commands.command(aliases=["serverroles"])
    async def roles(self, ctx):
        role_mentions = str([role.mention for role in ctx.message.guild.roles]).replace("[", "").replace("]", "").replace("'", "").replace(f"{ctx.message.guild.default_role.mention}, ", "@everyone, ")
        embed = discord.Embed(color=0xE9A72F)
        embed.set_author(icon_url=ctx.message.guild.icon_url, name="List of roles in {}".format(ctx.message.guild.name))
        embed.add_field(name="Roles:", value=role_mentions, inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["profilepicture", "avatar"])
    async def pfp(self, ctx, user: discord.Member = None):
        if user == None:
            emb = discord.Embed(title="Profile Picture of {}".format(ctx.message.author.name), color=0xE9A72F)
            emb.set_image(url=ctx.message.author.avatar_url)
            await ctx.send(embed=emb)
        else:
            embed = discord.Embed(title="Profile Picture of {}".format(user.name), color=0xE9A72F)
            embed.set_image(url=user.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["coin", "flipacoin"])
    async def coinflip(self, ctx):
        flip = random.choice(["The coin landed on heads💰", "The coin landed on tails💰"])
        await ctx.send(f"{flip}")

    @commands.command(aliases=["pong", "latency"])
    async def ping(self, ctx):
        # Time the time required to send a message first.
        # This is the time taken for the message to be sent, awaited, and then 
        # for discord to send an ACK TCP header back to you to say it has been
        # received; this is dependant on your bot's load (the event loop latency)
        # and generally how shit your computer is, as well as how badly discord
        # is behaving.
        start = time.monotonic()
        msg = await ctx.send('Pinging...')
        millis = (time.monotonic() - start) * 1000

        # Since sharded bots will have more than one latency, this will average them if needed.
        heartbeat = ctx.bot.latency * 1000

        await msg.edit(content=f'Heartbeat: {heartbeat:,.2f}ms\nACK: {millis:,.2f}ms.')
    
    @commands.command(aliases=["waffle", "gif"])
    async def wafflegif(self, ctx):
        gif = random.choice(["https://i.imgur.com/ZYtYt5O.gif", "https://i.imgur.com/hffKEIn.gif", "https://i.imgur.com/x9mg3Sj.gif", "https://i.imgur.com/0zlVS7w.gif", "https://i.imgur.com/ez4ZsMS.gif", "https://i.imgur.com/87Sl6.gif", "https://i.imgur.com/UnKylQk.gif", "https://i.imgur.com/S0MekgX.gif", "https://i.imgur.com/KieFRUb.gif", "https://i.imgur.com/3YrdkCz.gif", "https://i.imgur.com/8pbG99c.gif"])
        embed= discord.Embed(color=0xE9a72F)
        embed.set_image(url=f"{gif}")
        owneravi = self.bot.get_user(322449414142558208)
        embed.set_footer(icon_url=owneravi.avatar_url, text="Wafflebot by Alpha#5960")
        await ctx.send(embed=embed)

    @commands.command(aliases=["rockpaperscissors", "rock", "paper", "scissors"])
    async def rps(self, ctx, choice = None):
        if choice == None:
            error = discord.Embed(title="Error:", description="You didn't choose one of the 3 choices(Rock, Paper & Scissors).\n**Usage:** `w/rps [choice]`\n**Example:** `w/rps rock`", color=0xE73C24)
            await ctx.send(embed=error)
        rps = random.choice(["Rock", "Paper", "Scissors"])
        if choice == "paper":
            if rps == "Rock":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="**Paper** beats **rock**, which means you win!", color=0x15c513)
                await ctx.send(embed=embed)
            if rps == "Scissors":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="**Scissors** beat **paper**, which means I win!", color=0xE73C24)
                await ctx.send(embed=embed)
            if rps == "Paper":
                embed = discord.Embed(title=f"You chose Paper, I chose {rps}", description="It's a tie, which means no one wins!", color=0xE9A72F)
                await ctx.send(embed=embed)
        if choice == "rock":
            if rps == "Rock":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="It's a tie, which means no one wins!", color=0xE9A72F)
                await ctx.send(embed=embed)
            if rps == "Scissors":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="**Rock** beats **scissors**, which means you win!", color=0x15c513)
                await ctx.send(embed=embed)
            if rps == "Paper":
                embed = discord.Embed(title=f"You chose Rock, I chose {rps}", description="**Paper** beats **rock**, which means I win!", color=0xE73C24)
                await ctx.send(embed=embed)
        if choice == "scissors":
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
        if search == None:
            error = discord.Embed(title="Error:", description="You didn't sepcify a search request\n**Usage:** `w/rps [search]`\n**Example:** `w/wiki sausage`", color=0xE73C24)
            await ctx.send(embed=error)
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
        print("printout")
        wikipedia.set_lang(lang)
        try:
            wikipage = wikipedia.page(query)
            print("I found directly")
        except wikipedia.PageError:
            embe = discord.Embed(title="Error:", description="Cant access by default. Trying to search", color=0xE73C24)
            await ctx.send(embed=embe)
            print("Can't access by default. Trying to search")
        except wikipedia.DisambiguationError:
            embedd = discord.Embed(title="Error:", description="This search leads to a disambiguation page. Please be more specific.", color=0xE73C24)
            await ctx.send(embed=embedd)
            disambiguation = True
        except Exception:
            lookup = False
        if wikipage is None and lookup and not disambiguation:
            wikipage = wikipedia.suggest(query)
        if wikipage is None and lookup and not disambiguation:
            embed = discord.Embed(title="Error:", description=f"Sorry, cannot find {query}", color=0xE73C24)
            await ctx.send(embed=embed)
        elif not lookup:
            emb = discord.Embed(title="Error:", description="Something went wrong. Check the language, or maybe I can't reach Wikipedia")
            await ctx.send(embed=emb)
        else:
            imglist = wikipage.images
            if len(imglist) == 0:
                em = discord.Embed(title=wikipage.title, description=wikipedia.summary(query, sentences=2), colour=0xE9A72F, url=wikipage.url)
            else:
                em = discord.Embed(title=wikipage.title, description=wikipedia.summary(query, sentences=2), colour=0xE9A72F, url=wikipage.url, image=imglist[0])
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