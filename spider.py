import discord
from discord.ext import commands
import os
import random
import time

prefixes = ["spider ", "Spider ", "daddy ", "Daddy "]
spood = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes))
spood.remove_command("help")
spood.responses = [
                    "henlo", 
                    "is joke", 
                    "a", 
                    "stop talking about it please", 
                    "i'm not golfing", 
                    "lul", 
                    "*reacts with weeb emote*",
                    "<:zoomeyes:390046883281633290>", 
                    "that is the essential question",
                    "is this drama", 
                    "oh bOi",
                    "no", 
                    "yes", 
                    "maybe",
                    "how old are u 😄",
                    "Check in <#325648177178869760> idk",
                    "w0t",
                    "i see lol",
                    "lol sure.",
                    "this isnt the mee6 support server",
                    "java >>> *",
                    "doesn't everyone?",
                    "{0.mention} tf did you just say",
                    "like i said",
                    "Haha funny jokes",
                    "fucking hell"
                  ]
spood.last = None

@spood.event
async def on_message(msg):
    wew = await spood.get_context(msg)
    if msg.content.startswith("spider ") or msg.content.startswith("Spider ") or msg.content.startswith("Daddy ") or msg.content.startswith("daddy "):
        if not msg.author.bot:
            if not wew.command:
                await msg.channel.send(random.choice(spood.responses).format(msg.author))
            else:
                await spood.process_commands(msg)
        else:
            return



@spood.event
async def on_ready():
    print("Fine i'll get up..")
    print(f"i'm in {len(spood.guilds)}")


@spood.command()
async def help(ctx):
    skull = spood.get_user(158750488563679232)
    em = discord.Embed(title=f"sup {ctx.author.name}? it's me, Spider.", description="\n".join([f"`{cmd.name}` - {cmd.help}" for cmd in spood.commands if not cmd.name == "eval"]) + "\n or you could talk to me by saying `spider <something here>`", color=discord.Color.red())
    em.set_thumbnail(url=spood.user.avatar_url_as(format="png"))
    em.set_footer(text=f"Owned by {skull}", icon_url=skull.avatar_url_as(format="png"))
    
    await ctx.send(embed=em)


@spood.command()
async def source(ctx):
    """Curious about where the hell i came from?"""
    await ctx.send("Heres my github, enjoy nerd\nhttps://github.com/Skullbite/SpiderSim")

@spood.command(aliases=["e", "ev"])
async def eval(ctx, *, coolcode):
    """A real cool eval command"""
    values = {"spood": spood, "ctx": ctx, "_": spood.last}
    wew = discord.Embed()
    try:
      succ = eval(coolcode, values)
      wew.title = "Hey it worked"
      wew.color = discord.Color.green()
      wew.description = str(succ)
    except Exception as e:
      wew.title = "I fucked"
      wew.color = discord.Color.red()
      wew.description = str(e)
      
    await ctx.send(embed=wew)
      
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
        await ctx.send(content="", embed=embed)

@spood.command()
async def ping(ctx):
    """pong, you skid."""
    then = time.monotonic()
    
    wew = await ctx.send("fine nerd")
    now = round((time.monotonic() - then) * 1000)
    await wew.edit(content=f"pong. `{now}ms`")
    

async def on_command_error(ctx, err):
    if isinstance(err, errors.NoPrivateMessage):
        await ctx.send("This command can't be used in dms, sowwy.")

print("Lemme sleep some more...")
spood.run(os.environ["TOKEN"], restart=True) 
    
    
