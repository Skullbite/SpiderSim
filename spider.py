import discord
from discord.ext import commands
import os
import random

prefixes = ["spider ", "Spider "]
spood = commands.Bot(command_prefix=commands.when_mentioned_or(*def))
spood.responses = [
                    "henlo", 
                    "is joke", 
                    "a", 
                    "stop talking about it please", 
                    "i'm not golfing", 
                    "lul", 
                    "<:zoomeyes:390046883281633290>", 
                    "that is the essential question",
                    "is this drama", 
                    "oh bOi",
                    "no", 
                    "yes", 
                    "maybe",
                    "how old are u 😄",
                    "Check mod-log"
                  ]

@spood.event
async def on_message(msg):
    if msg.content.startswith("spider ") or msg.content.startswith("Spider "):
        await msg.channel.send(random.choice(spood.responses))
    else:
        await spood.process_commands(msg)


@spood.event
async def on_ready():
    print("Fine i'll do it.")


print("What do you want.")
spood.run(os.environ["TOKEN"], restart=True) 
    
    
