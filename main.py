import os

import discord
from dotenv import load_dotenv

import generator

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready() -> None:
    print(f'\nSuccessfully logged into Discord as "{bot.user}"\n')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.playing,
                                                        name="Shin Megami Tensei V"))


@bot.slash_command()
async def talk(ctx: discord.ApplicationContext) -> None:
    await ctx.respond(generator.generate())


@bot.slash_command()
async def create_joke(ctx: discord.ApplicationContext,
                      joke: str) -> None:
    await ctx.respond(joke)


@bot.slash_command()
async def answer(ctx: discord.ApplicationContext) -> None:
    await ctx.respond(generator.answer())

load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))
