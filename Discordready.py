import discord
import os
import random
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def okay(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)




@bot.command()
async def good(ctx):
    await ctx.send(f'Hallo')

@bot.command()
async def bye(ctx):
    await ctx.send("Papa" )


@bot.command()
async def Rex(ctx, times: int, content = 'Siema' ):
    

    for i in range(times):
        await ctx.send (content)

    

  
       
        



@bot.group()
async def Safe(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not Safe')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def human1(ctx):
    images = os.listdir('images')
    random_image = random.choice(images)
    with open(f'images/{random_image}', 'rb') as f:                        
        
        picture = discord.File(f)

    await ctx.send(file=picture)
    
@bot.command()
async def Human2(ctx):
    with open('images/Meme2.jpg', 'rb') as f:
       
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Human3(ctx):
    with open('images/Meme3.jpg', 'rb') as f:
    
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Human4(ctx):
    with open ('images/Meme4.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Human5(ctx):
    with open ('images/Meme5.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def Animal1(ctx):
    with open ('images/Memy6.jpeg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def Animal2(ctx):
    with open ('images/memy7.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Praca1(ctx):
    with open ('images/Memy8.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


    
@bot.command()
async def Praca2(ctx):
    with open ('images/Memy9.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


    
@bot.command()
async def Praca3(ctx):
    with open ('images/Memy10.jpg', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Goodcontry(ctx,):
    """Top 10 czyste kraje to..."""
    await ctx.send("Top 10 czystych krajow")
    await ctx.send("1. Islandia")
    await ctx.send("2.Finlandia")
    await ctx.send("3.Szwecja ")
    await ctx.send("4.Kanada")
    await ctx.send("5.Nowa Zelandia")
    await ctx.send("6.Australia")
    await ctx.send("7.Szwajcaria")
    await ctx.send("8.Norwegia")
    await ctx.send("9.Estonia")
    await ctx.send("10.Austria")
    
@bot.command()
async def Badcontry(ctx):
    
    """Top10Krajowzzanieczyszczeniemsrodowiskiem to..."""

    await ctx.send("Top10 Krajow z zanieczyszczeniem srodowiska")
    await ctx.send("1.Chiny")
    await ctx.send("2.Indie")
    await ctx.send("3.Stany Zjednoczone")
    await ctx.send("4.Rosja")
    await ctx.send("5.Brazylia")
    await ctx.send("6.Indonezja")
    await ctx.send("7.Pakistan")
    await ctx.send("8.Bangladesz")
    await ctx.send("9.Nigeria")
    await ctx.send("10.Egipt")



bot.run("Token")
