import discord
from discord.ext import commands

# Создаем экземпляр бота
bot = commands.Bot(command_prefix="/")

# Обрабатываем команду /hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет, {ctx.author.mention}!")

# Запускаем бота
bot.run("YOUR_BOT_TOKEN")
