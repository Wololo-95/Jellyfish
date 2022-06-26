import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import dotenv
import os

dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# allows bot to connect to server
intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(commands_prefix='$', intents=intents)

dev_server = 987859987374166126
main_server = 691695952855171153


@client.event
async def on_ready():
    print("Jellyfish 1.0 initiated...")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")


@client.slash_command(name="test", description="Tests the command function", guild_ids=[dev_server, main_server])
async def test(interaction: Interaction):
    await interaction.response.send_message("Plrrp")


@client.slash_command(name="join", description="Asks Jellyfish to join the active voice channel",guild_ids=[dev_server, main_server])
async def vc_join(interaction: Interaction):
    await interaction.response.send_message("Command not finished")

client.run(DISCORD_TOKEN)
