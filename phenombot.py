from discord.ext import commands
import discord
import variables
import os


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(variables.CHANNEL_ID)
    await channel.send("hello")

@bot.command()
async def upload(ctx):
    for file in os.listdir(variables.FILE_PATH):
        f = os.path.join(variables.FILE_PATH, file)
        await ctx.send(file=discord.File(f))

bot.run(variables.BOT_TOKEN)

