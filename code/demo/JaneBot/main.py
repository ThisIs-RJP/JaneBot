""" 
    Developed by RJ Paraiso
    This project is created and developed by me.
    All content, ideas, and work presented here are my own, unless otherwise stated. 
    
    Unauthorized use, reproduction, or distribution without my permission is prohibited.

    Jane Doe icon created by @O2H2_OH4 (Twitter)
"""

### Imports
import os, discord, random, Paginator

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
bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

## Loading token
load_dotenv("token.env")
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

    await bot.add_cog(AdminCom(bot))
    await bot.add_cog(FunCom(bot))

    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='and babysitting Sunday. Waiting for r!'))

@bot.event
async def on_command_error(ctx, error):
    print("Error encountered!")
    print(error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I have no idea what you're talking about :blush:")

@bot.command()
async def help(ctx, *, mes=None):
    if mes == None:
        await ctx.send(embed=help_embed("Command Categories", "> Fun\n> Admin", random.choice(COLORS)))
    
    elif mes != "help": ## If the user wants to know the details of a command
        ## TODO : we need some sort of error management here
        await Paginator.Simple().start(ctx, pages=help_paginator(mes.lower(), random.choice(COLORS)))

    elif mes.lower() in COMMANDS_LIST:
        await ctx.send(embed=help_embed(f"{mes.capitalize()} Commands", COMMANDS_LIST[mes.lower()], random.choice(COLORS)))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def ping_ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms - From GitLab! ♡ The pipelines look great!")


## Run bot
bot.run(TOKEN)
