import os, discord, datetime, string

from discord.ext          import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from outputs              import *
from outputs.embeds       import *


### Importing my cogs
class AdminCom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["purge"])
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed=title_embed("Messages cleared", 0x00FF7F))