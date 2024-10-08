import discord
from discord import app_commands, TextChannel
import json

bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)

def load(file):
    with open(file, "r") as file:
        return json.load(file)
    
def update_user(user):
    user_completion = load("./databases/user_data.json")
    catch_dates = load("./databases/catch_date.json")
    favorites = load("./databases/favorites_list.json")
    in_trade = load("./databases/in_trade.json")
    proposals = load("./databases/proposals.json")
    locked = load("./databases/locked.json")
    th_date = load("./databases/trade_history_date.json")
    with_who = load("./databases/trade_history_who.json")
    offer1 = load("./databases/trade_history_offer1.json")
    offer2 = load("./databases/trade_history_offer2.json")
    try:
        print(f"User @{user}: {user_completion[str(user.id)]}")
    except KeyError:
        with open("./databases/user_data.json", "r") as file:
            user_completion = json.load(file)
        user_completion[str(user.id)] = []
        with open("./databases/user_data.json", "w") as file:
            json.dump(user_completion, file)
    try:
        print(catch_dates[str(user.id)])
    except KeyError:
        with open("./databases/catch_date.json", "r") as file:
            catch_dates = json.load(file)
        catch_dates[str(user.id)] = []
        with open("./databases/catch_date.json", "w") as file:
            json.dump(catch_dates, file)
    try:
        print(favorites[str(user.id)])
    except KeyError:
        with open("./databases/favorites_list.json", "r") as file:
            favorites = json.load(file)
        favorites[str(user.id)] = []
        with open("./databases/favorites_list.json", "w") as file:
            json.dump(favorites, file)
    try:
        print(in_trade[str(user.id)])
    except KeyError:
        with open("./databases/in_trade.json", "r") as file:
            in_trade = json.load(file)
        in_trade[str(user.id)] = "False"
        with open("./databases/in_trade.json", "w") as file:
            json.dump(in_trade, file)
    try:
        print(proposals[str(user.id)])
    except KeyError:
        with open("./databases/proposals.json", "r") as file:
            proposals = json.load(file)
        proposals[str(user.id)] = []
        with open("./databases/proposals.json", "w") as file:
            json.dump(proposals, file)
    try:
        print(locked[str(user.id)])
    except KeyError:
        with open("./databases/locked.json", "r") as file:
            locked = json.load(file)
        locked[str(user.id)] = "False"
        with open("./databases/locked.json", "w") as file:
            json.dump(locked, file)
    try:
        print(th_date[str(user.id)])
    except KeyError:
        with open("./databases/trade_history_date.json", "r") as file:
            th_date = json.load(file)
        th_date[str(user.id)] = []
        with open("./databases/trade_history_who.json", "w") as file:
            json.dump(th_date, file)
    try:
        print(with_who[str(user.id)])
    except KeyError:
        with open("./databases/trade_history_who.json", "r") as file:
            with_who = json.load(file)
        with_who[str(user.id)] = []
        with open("./databases/trade_history_who.json", "w") as file:
            json.dump(with_who, file)
    try:
        print(offer1[str(user.id)])
    except KeyError:
        with open("./databases/trade_history_offer1.json", "r") as file:
            offer1 = json.load(file)
        offer1[str(user.id)] = []
        with open("./databases/trade_history_offer1.json", "w") as file:
            json.dump(offer1, file)
    try:
        print(offer2[str(user.id)])
    except KeyError:
        with open("./databases/trade_history_offer2.json", "r") as file:
            offer2 = json.load(file)
        offer2[str(user.id)] = []
        with open("./databases/trade_history_offer2.json", "w") as file:
            json.dump(offer2, file)

countryballs = load("./databases/countryball_list.json")
spawn_channel = load("./databases/channel_setup.json")
ball_image = load("./databases/countryball_images.json")
user_completion = load("./databases/user_data.json")
ball_emoji = load("./databases/emoji_ids.json")
catch_dates = load("./databases/catch_date.json")
favorites = load("./databases/favorites_list.json")
in_trade = load("./databases/in_trade.json")
proposals = load("./databases/proposals.json")
locked = load("./databases/locked.json")
th_date = load("./databases/trade_history_date.json")
with_who = load("./databases/trade_history_who.json")
offer1 = load("./databases/trade_history_offer1.json")
offer2 = load("./databases/trade_history_offer2.json")

class config_group(app_commands.Group):

    @app_commands.command(name="setup", description="Configures the bot's spawn channel!")
    @app_commands.checks.has_permissions(administrator=True)
    async def setup_config(self, interaction, channel: TextChannel):
        with open("./databases/channel_setup.json", "r") as file:
            spawn_channel = json.load(file)
        spawn_channel[str(interaction.guild.id)] = f"{channel.id}"
        with open("./databases/channel_setup.json", "w") as file:
            json.dump(spawn_channel, file)
        await interaction.response.send_message(f"Spawn channel setup in <#{channel.id}>!", ephemeral=False)
    @setup_config.error
    async def say_error(self, interaction, error):
        with open("./databases/channel_setup.json", "r") as file:
            spawn_channel = json.load(file)
        with open("./databases/channel_setup.json", "w") as file:
            json.dump(spawn_channel, file)
        await interaction.response.send_message("Hey you can't setup this bot, you're not the server admin.", ephemeral=False)

    @app_commands.command(name="disable", description="Disables spawning in a server.")
    @app_commands.checks.has_permissions(administrator=True)
    async def disable_spawn(self, interaction):
        with open("./databases/channel_setup.json", "r") as file:
            spawn_channel = json.load(file)
        spawn_channel[str(interaction.guild.id)] = ""
        with open("./databases/channel_setup.json", "w") as file:
            json.dump(spawn_channel, file)
        await interaction.response.send_message(f"Altball spawning is now disabled in {interaction.guild}, type /setup to re-enable spawning.", ephemeral=False)
    @disable_spawn.error
    async def disable_spawn_error(self, interaction, error):
        with open("./databases/channel_setup.json", "r") as file:
            spawn_channel = json.load(file)
        with open("./databases/channel_setup.json", "w") as file:
            json.dump(spawn_channel, file)
        await interaction.response.send_message("Hey you can't setup this bot, you're not the server admin.", ephemeral=False)

group1 = config_group(name="config")
