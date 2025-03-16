""" 
    String configuration files

    String classes: 
"""

## Imports
import random 
import discord

COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

## Strings
FIELDS_TIP: str = "Check our different commands! Run j!help for more information."

## Functions
def basic_embed(title: str, description: str, color: int) -> discord.Embed:

    embed = discord.Embed(title=title, description=description, color=random.choice(COLORS))

    embed.set_footer(text=FIELDS_TIP)

    return embed

def help_embed(title: str, description: str, color: int) -> discord.Embed:
    embed = discord.Embed(
        title       = title,
        description = description,
        timestamp   = discord.utils.utcnow()
    )

    embed.set_thumbnail(url="https://i.redd.it/oh2ho-oh4s-jane-drawings-are-so-adorable-v0-q845cip8jb1e1.png?width=900&format=png&auto=webp&s=3c7920f8e16058ac888d927d0d26bde9d39b9345")

    return embed

def title_embed(title: str, color: int) -> discord.Embed:
    embed = discord.Embed(title=title, color=random.choice(COLORS))

    return embed