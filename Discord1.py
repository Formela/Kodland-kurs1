import discord

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

bot.run("MTE5OTQxMzc3NDA4ODY3MTM1NA.GqYOUd.dnDqs5_SvPIvy8Nn_PxgkMs-NGY2d6UMJxyMFk")
