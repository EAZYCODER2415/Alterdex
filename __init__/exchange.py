import discord
from discord.ui import Select, View, Button, Modal
from discord import ui, app_commands, Member
import json
from datetime import datetime
import typing

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

class trade_group(app_commands.Group):
    
    @app_commands.command(name="begin", description="Begin trading with another user!")
    async def begin_trade(self, interaction, user: Member):
        in_trade = load("./databases/in_trade.json")
        if user.id != interaction.user.id and user.bot is False: # not yourself and not a bot
            update_user(user)
            update_user(interaction.user)
            if in_trade[str(interaction.user.id)] == "False" and in_trade[str(user.id)] == "False": # both users are not in a trade
                data0 = ""
                data1 = ""
                data1half = ""
                data2 = ""
                user1 = str(interaction.user.id)
                user2 = str(user.id)
                embed = discord.Embed(title="aa", description="embed", color=0xffffff)
                lock = Button(
                    label="Lock Proposal",
                    style=discord.ButtonStyle.secondary,
                    disabled=False,
                    emoji="🔒"
                )
                reset = Button(
                    label="Reset",
                    style=discord.ButtonStyle.secondary,
                    disabled=False,
                    emoji="💨"
                )
                cancel = Button(
                label="Cancel Trade",
                    style=discord.ButtonStyle.danger,
                    disabled=False,
                    emoji="❌"
                )
                async def lock_callback(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    locked[str(interaction.user.id)] = "True"
                    with open("./databases/locked.json", "w") as file:
                        json.dump(locked, file)
                    lock.disabled = True
                    reset.disabled = True
                    ball_emoji = load("./databases/emoji_ids.json")
                    if str(interaction.user.id) == user1:
                        if locked[user1] == "True":
                            data0 = ":lock: "
                        data0 += interaction.user.name
                        if len(proposals[user1]) == 0:
                            data1 = "*Empty*"
                        else:
                            data1 = ""
                            for altball in proposals[user1]:
                                data1 += ball_emoji[altball] + altball + "\n"
                    else:
                        if locked[user2] == "True":
                            data1half = ":lock: "
                        data1half += user.name
                        if len(proposals[user2]) == 0:
                            data2 = "*Empty*"
                        else:
                            data2 = ""
                            for altball in proposals[user2]:
                                data2 += ball_emoji[altball] + altball + "\n"
                    embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                    await interaction.response.edit_message(embed=embed, view=view, ephemeral=True)

                async def reset_callback(interaction):
                    await interaction.response.send_message(f"nigga")

                async def cancel_callback(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    lock.disabled = True
                    reset.disabled = True
                    cancel.disabled = True
                    if locked[user1] == "True":
                        locked[user1] = "False"
                    if locked[user2] == "True":
                        locked[user2] = "False"
                    in_trade[user1] = "False"
                    in_trade[user2] = "False"
                    with open("./databases/locked.json", "w") as file:
                        json.dump(locked, file)
                    with open("./databases/in_trade.json", "w") as file:
                        json.dump(in_trade, file)
                    embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Trade has been canceled.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                    await interaction.response.edit_message(embed=embed, view=view, ephemeral=True)

                async def on_timeout(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    lock.disabled = True
                    reset.disabled = True
                    cancel.disabled = True
                    if locked[user1] == "True":
                        locked[user1] = "False"
                    if locked[user2] == "True":
                        locked[user2] = "False"
                    in_trade[user1] = "False"
                    in_trade[user2] = "False"
                    with open("./databases/locked.json", "w") as file:
                        json.dump(locked, file)
                    with open("./databases/in_trade.json", "w") as file:
                        json.dump(in_trade, file)
                    embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Trade has been canceled due to inactivity. Try again later.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                    await interaction.response.edit_message(embed=embed, view=view, ephemeral=True)

                lock.callback = lock_callback
                reset.callback = reset_callback
                cancel.callback = cancel_callback
                view = View(timeout=900.0)
                view.add_item(lock)
                view.add_item(reset)
                view.add_item(cancel)
                in_trade[str(interaction.user.id)] = "True"
                in_trade[str(user.id)] = "True"
                locked[str(interaction.user.id)] = "False"
                locked[str(user.id)] = "False"
                proposals[str(interaction.user.id)] = []
                proposals[str(user.id)] = []
                with open("./databases/locked.json", "w") as file:
                    json.dump(locked, file)
                with open("./databases/in_trade.json", "w") as file:
                    json.dump(in_trade, file)
                with open("./databases/proposals.json", "w") as file:
                    json.dump(proposals, file)
                ball_emoji = load("./databases/emoji_ids.json")
                data0 = f''':lock: {interaction.user.name}''' 
                data1 = "*Empty*"
                data1half = f''':lock: {user.name}''' 
                data2 = "*Empty*"
                embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                await interaction.response.send_message(embed=embed, view=view, ephemeral=False)
            else:
                await interaction.response.send_message("Either the user or you are in a trading session at the moment, please try again later.", ephemeral=False)
        else:
            await interaction.response.send_message(f'''You cannot propose a trade with:
- **Bots**
- **Yourself**
Try again.''')

    @app_commands.command(name="add", description="Add a countryball into your trading proposal!")
    async def add_trade(self, interaction, countryball: str):
        update_user(interaction.user)
        if in_trade[str(interaction.user.id)] == "True" and locked[str(interaction.user.id)] == "False":
            # if statement whether it is a favortie
            await interaction.response.send_message(f"Added {countryball}!", ephemeral=False)
        elif locked[str(interaction.user.id)] == "True":
            await interaction.response.send_message(f"You've locked your proposal, can't change it anymore.", ephemeral=True)
        elif in_trade[str(interaction.user.id)] == "False":
            await interaction.response.send_message(f"You are not in an ongoing trade.", ephemeral=True)
        
    @add_trade.autocomplete("countryball")
    async def add_trade_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        user_completion = load("./databases/user_data.json")
        for countryball_option in user_completion[str(interaction.user.id)]:
            if countryball_option not in proposals[str(interaction.user.id)]:
                favorites = load("./databases/favorites_list.json")
                inList = False
                for i in range(len(favorites[str(interaction.user.id)])):
                    if (favorites[str(interaction.user.id)][i] == countryball_option):
                        inList = True
                if (inList):
                    data.append(app_commands.Choice(name=f"❤️ {countryball_option}", value=countryball_option))
                else:
                    data.append(app_commands.Choice(name=countryball_option, value=countryball_option))
        return data

group3 = trade_group(name="exchange")
