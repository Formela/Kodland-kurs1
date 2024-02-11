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



bot.run("Token")
