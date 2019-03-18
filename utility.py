def getEmbedColour(colour: str):
    if colour.lower() == "default":
        return 0x363941 #'Invisible' colour code
    elif colour.lower() == "green":
        return 0x26d934 #Green colour code
    elif colour.lower() == "red":
        return 0xE73C24 #Red colour code
    elif colour.lower() == "yellow":
        return 0xFFFF00 #Yellow colour code
    elif colour.lower() == "waffle":
        return 0xE9A72F #Classic waffle colour code

def getEmoji(type: str):
    if type.lower() == "red_tick":
        return "<:redtick:506537775642968095>"
    elif type.lower() == "green_tick":
        return "<:greentick:506537759532515330>"

def guild_owner(ctx):
    if ctx.author == ctx.guild.owner:
        return True
    else: 
        return False

#if bot.user.permissions_in(bot.get_channel(ID)).add_reactions == True: