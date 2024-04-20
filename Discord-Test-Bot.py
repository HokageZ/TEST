import discord
from discord.ext import commands

# Define bot's command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Command: Greet
@bot.command()
async def greet(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')
