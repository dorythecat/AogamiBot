import os

import discord
from dotenv import load_dotenv

import requests

import generator

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)

load_dotenv()

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


@bot.slash_command()
async def image(ctx: discord.ApplicationContext) -> None:
    r = requests.get(f'https://danbooru.donmai.us/posts/random?q=shin_megami_tensei',
                     auth=(os.getenv("DANBOORU_USER"), os.getenv("DANBOORU_API_KEY")))
    if r.status_code != 200:
        await ctx.respond("Young man, my image dealer gave me this for you: RESPONSE CODE " + str(r.status_code))
    await ctx.respond(f"Young man, [here]({r.url}) I have found a treasured picture of me and my friends. Please keep it safe.")

bot.run(os.getenv("BOT_TOKEN"))
