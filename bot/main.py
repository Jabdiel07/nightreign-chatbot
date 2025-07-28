from discord.commands import Option, SlashCommandGroup
#from logging_config import setup_logging
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

name_lookup, category_lookup = load_game_data() # loading the results of the load_game_data function into two dictionaries respectively

char_fields = ["description", "lore", "weapon_preference", "passive_ability", "skill_ability", "ultimate_art", "scaling"] # list that contains the fields we care about for characters

boss_fields = ["description", "lore", "weakness", "immunity", "resistance"] # list that contains the fields we care about for bosses

category = SlashCommandGroup("category", "Get info on a character or boss.", guild_ids = [612816995754180655]) # this is creating the base format for the slash command. The first argument is the name we're going to use to invoke the slash command, so /category in this case, and the second argument is the description that appears to the user that tell them what the command does. The third argument sets the server id so it doesn't take too long for the slash commands to update

# this event right here is tied to the character choice. The function does the usual, it asks the user for which character they want info for and then they pick the field they're interested in.
@category.command(name="character", description = "Look up a Nightfarer's attributes.")
async def character_info(ctx, name = Option(str, "Which character?", choices = category_lookup["character"]), field = Option(str, "Which field to show?", choices = char_fields)):
    logger.info(f"{field} Query initiated by {ctx.author.name} for {name}")
    entry = name_lookup[name.lower()]
    value = entry.get(field) or "No data available."
    pretty_field = field.replace("_", " ").title() #.title() converts the field string into a title case, capitalizing the first letter of each word and lowercases the rest
    await ctx.respond(f"**{name}** — *{pretty_field}*: {value}")

# same as the previous event, but this time for bosses
@category.command(name="boss", description = "Look up a Nightlord's attribute.")
async def boss_info(ctx, name = Option(str, "Which boss", choices = category_lookup["boss"]), field = Option(str, "Which field to show?", choices = boss_fields)):
    logger.info(f"{field} Query initiated by {ctx.author.name} for {name}")
    entry = name_lookup[name.lower()]
    value = entry.get(field) or "No data available."
    pretty_field = field.replace("_", " ").title()
    await ctx.respond(f"**{name}** — *{pretty_field}*: {value}")

bot.add_application_command(category) # this line right here ensures that both slash commands we defined for characters and bosses are registered to the Discord bot. If we declared the slash command like we did in the translator bot (@bot.slash_command(...)), then Discord would be able to detect the slash command automatically. Since we defined the slash command in a different way this time, then this line is necessary so Discord can recognize the group (that's the category = SlashCommandGroup we defined) and its subcommands (the character and boss functions)

@bot.event
async def on_ready():
    await bot.sync_commands() # this line is optional, pretty much all it does is register all the commands you defined a lot faster (without this line, it could take up to an hour for them to register)
    logger.info(f"{bot.user} has connected to Discord.")

@bot.command(name = "hello")
async def hello(ctx):
    print(f"Hello command invoked by {ctx.author.name}")
    await ctx.send("Hello, I'm alive!")

if not DISCORD_TOKEN:
    logger.error("Please, check your Discord Token.")
    exit(1)

bot.run(DISCORD_TOKEN)