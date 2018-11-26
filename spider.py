import discord
from discord.ext import commands
import os
import random

prefixes = ["spider ", "Spider "]
spood = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes))
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

@spood.command()
@commands.guild_only()
async def server(ctx):
    """ Check info about current server """
    if ctx.invoked_subcommand is None:
        findbots = sum(1 for member in ctx.guild.members if member.bot)

        embed = discord.Embed()
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Bots", value=findbots, inline=True)
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Region", value=ctx.guild.region, inline=True)
        embed.add_field(name="Emojis", value=" ".join([f"<:{x.name}:{x.id}>" for x in ctx.guild.emojis if not x.animated]) + " " + " ".join([f"<a:{x.name}:{x.id}>" for x in ctx.guild.emojis if x.animated]))
        embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
        await ctx.send(content="", embed=embed)

async def on_command_error(ctx, err):
    if isinstance(err, errors.NoPrivateMessage):
        await ctx.send("This command can't be used in dms, sowwy.")

print("What do you want.")
spood.run(os.environ["TOKEN"], restart=True) 
    
    
