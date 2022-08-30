from os import getenv
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

# Read discord bot settings
load_dotenv()
bot_token = getenv("BOT_TOKEN")

# Defining the bot and settings
client = commands.InteractionBot(
    name = "NX_Debugger - v.1.0.0",
    sync_commands = True,
    intents = disnake.Intents.all()
)

# Initialize the bot
cogs = ["error_reader", "errors", "events", "invite", "NX_OBD1", "presence"]
for extention in cogs:
    try:
        client.load_extension("cogs." + extention)
    except Exception as error:
        print(f"Unable to load {extention} {error}.")

try:
    client.run(bot_token)
except Exception as error:
    print(f"Error when logging in: {error}")
