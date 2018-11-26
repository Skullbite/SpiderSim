import discord
from discord.ext import commands
import os
import random

prefixes = ["spider ", "Spider "]
spood = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes))
spood.remove_command("help")
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
    wew = await spood.get_context(msg)
    if msg.content.startswith("spider ") or msg.content.startswith("Spider "):
        if not wew.command:
            await msg.channel.send(random.choice(spood.responses))
        else:
            await spood.process_commands(msg)
    else:
        await spood.process_commands(msg)


@spood.event
async def on_ready():
    print("Fine i'll do it.")


@spood.command()
async def help(ctx):
    skull = spood.get_user(158750488563679232)
    em = discord.Embed(title=f"sup {ctx.author.name}? it's me, Spider.", description="\n".join([f"`{cmd.name}` - {cmd.help}" for cmd in spood.commands]) + "\n or you could talk to me by saying `spider <something here>`", color=discord.Color.red())
    em.set_thumbnail(url=spood.user.avatar_url_as(format="png"))
    em.set_footer(text=f"Owned by {skull}", icon_url=skull.avatar_url_as(format="png"))
    
    await ctx.send(embed=em)


@spood.command()
async def source(ctx):
    """Curious about where the hell i came from?"""
    await ctx.send("Heres my github, enjoy nerd\nhttps://github.com/Skullbite/SpiderSim")
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
    
    
