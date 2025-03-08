""" 
    Developed by RJ Paraiso
    This project is created and developed by me.
    All content, ideas, and work presented here are my own, unless otherwise stated. 
    
    Unauthorized use, reproduction, or distribution without my permission is prohibited.

    Jane Doe icon created by @O2H2_OH4 (Twitter)
"""

### Imports
import os, discord, random

from discord.ext          import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from dotenv               import load_dotenv, find_dotenv

## String Configuration Files
from outputs.admin  import *
from outputs.embeds import *
from outputs.help   import *

## Cog Imports
from cogs.admin import *
from cogs.fun import *

## Command Prefix
bot = commands.Bot(command_prefix="j!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

## Loading token
load_dotenv("token.env")
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

    await bot.add_cog(AdminCom(bot))
    await bot.add_cog(FunCom(bot))

    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='you... Waiting for j!'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I have no idea what you're talking about :blush:")

@bot.command()
async def help(ctx, *, mes=None):
    if mes == None:
        await ctx.send(embed=help_embed("Command Categories", "> Fun\n> Admin", random.choice(COLORS)))
    
    # elif mes != "help": ## If the user wants to know the details of a command
        # pass
    # 

        # TODO
    
    elif mes.lower() in COMMANDS_LIST:
        await ctx.send(embed=help_embed(f"{mes.capitalize()} Commands", COMMANDS_LIST[mes.lower()], random.choice(COLORS)))


## Run bot
bot.run(TOKEN)