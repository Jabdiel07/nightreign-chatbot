from discord.commands import Option, SlashCommandGroup
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from data_loader import load_game_data
from logger_info import setup_logging

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

logger = setup_logging(level=os.getenv("LOG_LEVEL", "INFO"))

logger.info("Starting Nightreign Bot")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix ="!", intents=intents)

# load the results of the load_game_data function into two dictionaries respectively
name_lookup, category_lookup = load_game_data()

# create two lists that contain character and boss fields respectively
char_fields = ["description", "lore", "weapon_preference", "passive_ability", "skill_ability", "ultimate_art", "scaling"]

boss_fields = ["description", "lore", "weakness", "immunity", "resistance"]

# base format for the slash command, it also sets the server id where the bot will be used at and more can be added to it
category = SlashCommandGroup("category", "Get info on a character or boss.", guild_ids = [612816995754180655])

# event for character choice
@category.command(name="character", description = "Look up a Nightfarer's attributes.")
async def character_info(ctx, name = Option(str, "Which character?", choices = category_lookup["character"]), field = Option(str, "Which field to show?", choices = char_fields)):
    logger.info(f"{field} Query initiated by {ctx.author.name} for {name}")
    entry = name_lookup[name.lower()]
    value = entry.get(field) or "No data available."
    pretty_field = field.replace("_", " ").title() #.title() converts the field string into a title case, capitalizing the first letter of each word and lowercases the rest
    await ctx.respond(f"**{name}** — *{pretty_field}*: {value}")

# event for boss choice
@category.command(name="boss", description = "Look up a Nightlord's attribute.")
async def boss_info(ctx, name = Option(str, "Which boss", choices = category_lookup["boss"]), field = Option(str, "Which field to show?", choices = boss_fields)):
    logger.info(f"{field} Query initiated by {ctx.author.name} for {name}")
    entry = name_lookup[name.lower()]
    value = entry.get(field) or "No data available."
    pretty_field = field.replace("_", " ").title()
    await ctx.respond(f"**{name}** — *{pretty_field}*: {value}")

# ensure we register the character and boss commands to the Discord bot
bot.add_application_command(category)

@bot.event
async def on_ready():
    await bot.sync_commands() # registers the defined commands in a timely manner
    logger.info(f"{bot.user} has connected to Discord.")

@bot.command(name = "hello")
async def hello(ctx):
    print(f"Hello command invoked by {ctx.author.name}")
    await ctx.send("Hello, I'm alive!")

if not DISCORD_TOKEN:
    logger.error("Please, check your Discord Token.")
    exit(1)

bot.run(DISCORD_TOKEN)