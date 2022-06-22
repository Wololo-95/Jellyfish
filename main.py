# Import Discord.py - allow access to discord API
import discord

import os
import random
import dotenv

# load environmental variables
dotenv.load_dotenv()

# Attempts to load the .env file containing bot token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Obtain discord client object - defined in discord.py CLIENT = BOT
bot = discord.Client()


# Event listener for when bot offline -> online
@bot.event
async def on_ready():
    # Creates counter to know how many servers the bot is connected to
    chat_count = 0

    # Loops through servers associated with bot
    for guild in bot.guilds:
        # Print server name and id
        print(f"- {guild.id} (name: {guild.name})")
        # Increment the guild counter
        chat_count = chat_count + 1

    # Prints value of chat_count (# servers bot is in)
    print("Jellyfish is in" + str(chat_count) + "guilds/servers.")


# Event listener for when a new message is sent to a channel
@bot.event
async def on_message(message):
    # Checks to see if the message contains a given string
    if message.content == "hello":
        # Returns message to channel
        await message.channel.send("Plrrrp")
    if message.content == "joey":
        await message.channel.send("https://c.tenor.com/7Z_C25O8SiUAAAAM/joey-hero.gif")
    if message.content == "mick":
        await message.channel.send("https://tenor.com/view/narcissism-spongebob-gif-21467726")
    if message.content == "bobby":
        await message.channel.send("fuck u bobby")


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.voice_channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Runs bot on specified hidden token
bot.run(DISCORD_TOKEN)
