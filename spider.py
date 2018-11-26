import discord
from discord.ext import commands
import os
import randim

def = ["spider ", "Spider "]
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
    print("Am ready to do stuff")


print("am loading gimme a bit.")
spood.run(os.environ["TOKEN"], restart=True) 
    
    
