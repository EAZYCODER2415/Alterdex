import discord
from discord.ui import Select, View, Button, Modal
from discord import ui, app_commands, Member
import json
from datetime import datetime
import typing
from discord.ext import tasks

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

class trade_group(app_commands.Group):
    
    @app_commands.command(name="begin", description="Begin trading with another user!")
    async def begin_trade(self, interaction, user: Member):
        in_trade = load("./databases/in_trade.json")
        if user.id != interaction.user.id and user.bot is False: # not yourself and not a bot
            update_user(user)
            update_user(interaction.user)
            if in_trade[str(interaction.user.id)] == "False" and in_trade[str(user.id)] == "False": # both users are not in a trade
                global data0, data1, data1half, data2, user1, user2, test, count, user1_name, user2_name, url
                data0 = ""
                data1 = ""
                data1half = ""
                data2 = ""
                count = 0
                user1 = str(interaction.user.id)
                user2 = str(user.id)
                user1_name = interaction.user.name
                user2_name = user.name
                url = ""
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
                @tasks.loop(seconds=1.0)
                async def edit_session():
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    global test
                    global view
                    global count
                    global url
                    proposals = load("./databases/proposals.json")
                    in_trade = load("./databases/in_trade.json")
                    if (in_trade[user1] == "True" and in_trade[user2] == "True") and count >= 1:
                        ball_emoji = load("./databases/emoji_ids.json")
                        if len(proposals[user1]) == 0:
                            data1 = "*Empty*"
                        else:
                            data1 = ""
                            for altball in proposals[user1]:
                                if proposals[user1].index(altball) >= 1:
                                    data1 += "\n"
                                data1 += ball_emoji[altball] + " " + altball
                        if len(proposals[user2]) == 0:
                            data2 = "*Empty*"
                        else:
                            data2 = ""
                            for altball in proposals[user2]:
                                if proposals[user2].index(altball) >= 1:
                                    data2 += "\n"
                                data2 += ball_emoji[altball] + " " + altball
                        with open("./databases/proposals.json", "w") as file:
                            json.dump(proposals, file)
                        embed = discord.Embed(title=f'''**<@{user1}> has proposed a trade with <@{user2}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                        test = await interaction.edit_original_response(embed=embed, view=view)
                        test = interaction.response
                    count += 1

                async def lock_callback(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    global user1_name
                    global user2_name
                    global test
                    if str(interaction.user.id) == user1 or str(interaction.user.id) == user2:
                        locked = load("./databases/locked.json")
                        if locked[str(interaction.user.id)] == "False":
                            proposals = load("./databases/proposals.json")
                            locked[str(interaction.user.id)] = "True"
                            with open("./databases/locked.json", "w") as file:
                                json.dump(locked, file)
                            ball_emoji = load("./databases/emoji_ids.json")
                            if str(interaction.user.id) == user1:
                                if locked[user1] == "True":
                                    data0 = ":lock: "
                                data0 += user1_name
                                if len(proposals[user1]) == 0:
                                    data1 = "*Empty*"
                                else:
                                    data1 = ""
                                    for altball in proposals[user1]:
                                        if proposals[user1].index(altball) >= 1:
                                            data1 += "\n"
                                        data1 += ball_emoji[altball] + " " + altball
                            else:
                                if locked[user2] == "True":
                                    data1half = ":lock: "
                                data1half += user2_name
                                if len(proposals[user2]) == 0:
                                    data2 = "*Empty*"
                                else:
                                    data2 = ""
                                    for altball in proposals[user2]:
                                        if proposals[user2].index(altball) >= 1:
                                            data2 += "\n"
                                        data2 += ball_emoji[altball] + " " + altball
                            embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                            if locked[user1] == "True" and locked[user2] == "True":
                                # trade confirmation
                                global url
                                lock.disabled = True
                                reset.disabled = True
                                cancel.disabled = True
                                data0 = ":white_check_mark: "
                                data0 += user1_name
                                data1half = ":white_check_mark: "
                                data1half += user2_name
                                embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Trade successful! Both traders confirmed their session!*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x2ecc71)
                                locked[user1] = "False"
                                locked[user2] = "False"
                                in_trade[user1] = "False"
                                in_trade[user2] = "False"
                                proposals[user1] = []
                                proposals[user2] = []
                                url = ""
                                with open("./databases/locked.json", "w") as file:
                                    json.dump(locked, file)
                                with open("./databases/in_trade.json", "w") as file:
                                    json.dump(in_trade, file)
                                with open("./databases/proposals.json", "w") as file:
                                    json.dump(proposals, file)
                                edit_session.stop()
                                test = await interaction.response.edit_message(embed=embed, view=view)
                                pass
                            test = await interaction.response.edit_message(embed=embed, view=view)
                            test = interaction.response
                        else:
                            await interaction.response.send_message("You've already locked your proposal.", ephemeral=True)
                    else:
                        await interaction.response.send_message("Butt out, you're not part of this trade.", ephemeral=True)

                async def reset_callback(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    global test
                    if str(interaction.user.id) == user1 or str(interaction.user.id) == user2:
                        locked = load("./databases/locked.json")
                        if locked[str(interaction.user.id)] == "False":
                            ball_emoji = load("./databases/emoji_ids.json")
                            if str(interaction.user.id) == user1:
                                proposals[user1] = []
                                if len(proposals[user1]) == 0:
                                    data1 = "*Empty*"
                                else:
                                    data1 = ""
                                    for altball in proposals[user1]:
                                        if proposals[user1].index(altball) >= 1:
                                            data1 += "\n"
                                        data1 += ball_emoji[altball] + " " + altball
                            else:
                                proposals[user2] = []
                                if len(proposals[user2]) == 0:
                                    data2 = "*Empty*"
                                else:
                                    data2 = ""
                                    for altball in proposals[user2]:
                                        if proposals[user2].index(altball) >= 1:
                                            data2 += "\n"
                                        data2 += ball_emoji[altball] + " " + altball
                            with open("./databases/proposals.json", "w") as file:
                                json.dump(proposals, file)
                            embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                            test = await interaction.response.edit_message(embed=embed, view=view)
                            test = interaction.response
                        else:
                            await interaction.response.send_message("You've already locked your proposal.", ephemeral=True)
                    else:
                        await interaction.response.send_message("Butt out, you're not part of this trade.", ephemeral=True)

                async def cancel_callback(interaction):
                    if str(interaction.user.id) == user1 or str(interaction.user.id) == user2:
                        global data0
                        global data1
                        global data1half
                        global data2
                        global user1
                        global user2
                        global test
                        global url
                        lock.disabled = True
                        reset.disabled = True
                        cancel.disabled = True
                        if locked[user1] == "True":
                            locked[user1] = "False"
                        if locked[user2] == "True":
                            locked[user2] = "False"
                        in_trade[user1] = "False"
                        in_trade[user2] = "False"
                        proposals[user1] = []
                        proposals[user2] = []
                        url = ""
                        with open("./databases/locked.json", "w") as file:
                            json.dump(locked, file)
                        with open("./databases/in_trade.json", "w") as file:
                            json.dump(in_trade, file)
                        with open("./databases/proposals.json", "w") as file:
                            json.dump(proposals, file)
                        if str(interaction.user.id) == user1:
                            data0 = ":no_entry_sign: "
                            data0 += user1_name
                            if len(proposals[user1]) == 0:
                                data1 = "*Empty*"
                            else:
                                data1 = ""
                                for altball in proposals[user1]:
                                    if proposals[user1].index(altball) >= 1:
                                        data1 += "\n"
                                    data1 += ball_emoji[altball] + " " + altball
                        elif str(interaction.user.id) == user2:
                            data1half = ":no_entry_sign: "
                            data1half += user2_name
                            if len(proposals[user2]) == 0:
                                data2 = "*Empty*"
                            else:
                                data2 = ""
                                for altball in proposals[user2]:
                                    if proposals[user2].index(altball) >= 1:
                                        data2 += "\n"
                                    data2 += ball_emoji[altball] + " " + altball
                        embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Trade has been canceled.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0xe74c3c)
                        edit_session.stop()
                        test = await interaction.response.edit_message(embed=embed, view=view)
                    else:
                        await interaction.response.send_message("Butt out, you're not part of this trade.", ephemeral=True)

                async def on_timeout(interaction):
                    global data0
                    global data1
                    global data1half
                    global data2
                    global user1
                    global user2
                    global test
                    global url
                    lock.disabled = True
                    reset.disabled = True
                    cancel.disabled = True
                    in_trade[user1] = "True"
                    in_trade[user2] = "True"
                    locked[user1] = "False"
                    locked[user2] = "False"
                    proposals[user1] = []
                    proposals[user2] = []
                    url = ""
                    with open("./databases/locked.json", "w") as file:
                        json.dump(locked, file)
                    with open("./databases/in_trade.json", "w") as file:
                        json.dump(in_trade, file)
                    with open("./databases/proposals.json", "w") as file:
                        json.dump(proposals, file)
                    embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Trade has been canceled due to inactivity. Try again later.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0xe74c3c)
                    edit_session.stop()
                    test = await interaction.response.edit_message(embed=embed, view=view)

                lock.callback = lock_callback
                reset.callback = reset_callback
                cancel.callback = cancel_callback
                global view
                view = View(timeout=900.0)
                view.add_item(lock)
                view.add_item(reset)
                view.add_item(cancel)
                in_trade[user1] = "True"
                in_trade[user2] = "True"
                locked[user1] = "False"
                locked[user2] = "False"
                proposals[user1] = []
                proposals[user2] = []
                with open("./databases/locked.json", "w") as file:
                    json.dump(locked, file)
                with open("./databases/in_trade.json", "w") as file:
                    json.dump(in_trade, file)
                with open("./databases/proposals.json", "w") as file:
                    json.dump(proposals, file)
                data0 = f'''{interaction.user.name}''' 
                data1 = "*Empty*"
                data1half = f'''{user.name}''' 
                data2 = "*Empty*"
                embed = discord.Embed(title=f'''**<@{interaction.user.id}> has proposed a trade with <@{user.id}>**''', description=f'''Add or remove Altballs you want to trade using the **/exchange add** and **/exchange remove** commands. Once you're finished with your offer, click the lock proposal button below to confirm and wait for your partner to finish.

*Both trading partners have 30 minutes before this interaction ends.*
**{data0}**
{data1}
**{data1half}**
{data2}''', color=0x9b59b6)
                test = await interaction.response.send_message(embed=embed, view=view, ephemeral=False)
                test = interaction.response
                url = await interaction.original_response()
                url = url.jump_url
                await edit_session.start()
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
        in_trade = load("./databases/in_trade.json")
        proposals = load("./databases/proposals.json")
        locked = load("./databases/locked.json")
        if in_trade[str(interaction.user.id)] == "True" and locked[str(interaction.user.id)] == "False": # in a trade and haven;t locked
            if countryball == "none":
                await interaction.response.send_message("There are no Altballs to add, go collect some.", ephemeral=True)
            else:
                if (countryball in favorites[str(interaction.user.id)]):
                    favorites[str(interaction.user.id)].remove(countryball)
                    with open("./databases/favorites_list.json", "w") as file:
                        json.dump(favorites, file)
                proposals[str(interaction.user.id)].append(countryball)
                with open("./databases/proposals.json", "w") as file:
                    json.dump(proposals, file)
                await interaction.response.send_message(f"Added **{countryball}** into trade offer!", ephemeral=True)
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
        if len(user_completion[str(interaction.user.id)]) == 0:
            data.append(app_commands.Choice(name="No Altballs in your inventory.", value="none"))
        else:
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
    
    @app_commands.command(name="remove", description="Remove a countryball from your trading proposal!")
    async def remove_trade(self, interaction, countryball: str):
        update_user(interaction.user)
        in_trade = load("./databases/in_trade.json")
        proposals = load("./databases/proposals.json")
        locked = load("./databases/locked.json")
        if in_trade[str(interaction.user.id)] == "True" and locked[str(interaction.user.id)] == "False": # in a trade and haven;t locked
            if countryball == "none":
                await interaction.response.send_message("There are no Altballs to remove, try again.", ephemeral=True)
            else:
                proposals[str(interaction.user.id)].remove(countryball)
                with open("./databases/proposals.json", "w") as file:
                    json.dump(proposals, file)
                await interaction.response.send_message(f"Removed **{countryball}** from trade offer!", ephemeral=True)
        elif locked[str(interaction.user.id)] == "True":
            await interaction.response.send_message(f"You've locked your proposal, can't change it anymore.", ephemeral=True)
        elif in_trade[str(interaction.user.id)] == "False":
            await interaction.response.send_message(f"You are not in an ongoing trade.", ephemeral=True)
        
    @remove_trade.autocomplete("countryball")
    async def remove_trade_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        proposals = load("./databases/proposals.json")
        if len(proposals[str(interaction.user.id)]) == 0:
            data.append(app_commands.Choice(name="No Altballs in the offer.", value="none"))
        else:
            for countryball_option in proposals[str(interaction.user.id)]:
                data.append(app_commands.Choice(name=countryball_option, value=countryball_option))
        return data

    @app_commands.command(name="redirect", description="Navigate back to your trading session!")
    async def redirect_link(self, interaction):
        update_user(interaction.user)
        in_trade = load("./databases/in_trade.json")
        if in_trade[str(interaction.user.id)] == "True":
            global url
            global user1, user2
            if str(interaction.user.id) == user1 or str(interaction.user.id) == user2:
                await interaction.response.send_message(f"[:point_right: Click here to return to trading session!]({url})", ephemeral=False)
            else:
                await interaction.response.send_message(f"An error occurred, please try again later.", ephemeral=False)
        else:
            await interaction.response.send_message(f"You are not in an ongoing trade.", ephemeral=True)

    @app_commands.command(name="history", description="View your Altball trading history!")
    async def trading_history(self, interaction):
        update_user(interaction.user)
        countryballs = load("./databases/countryball_list.json")
        ball_emoji = load("./databases/emoji_ids.json")
        embeds = []
        toIndex = 0
        maxPages = int(len(countryballs["countryball"]) / 5) + 1
        if (len(countryballs["countryball"]) % 5 == 0):
            maxPages -= 1
        index = 0
        desc = ""
        divisor = 1
        temp = 0
        while (index < maxPages):
            desc = f'''Altball rarity'''
            toIndex = 5 * divisor 
            j = temp
            while (j < toIndex):
                try:
                    if (j == 0):
                        desc += f'''
**{countryballs["countryball"][j]}**
{ball_emoji[countryballs["countryball"][j]]} Rarity: 0.99'''
                    else:
                        desc += f'''
**{countryballs["countryball"][j]}**
{ball_emoji[countryballs["countryball"][j]]} Rarity: {round((len(countryballs["countryball"]) - j) / len(countryballs["countryball"]), 2)}'''
                    temp += 1
                except IndexError:
                    pass
                j += 1
            divisor += 1
            embed = discord.Embed(title="", description=desc, color=0xfce33f)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
            embed.set_footer(text=f"Page {index+1}/{maxPages}")
            embeds.append(embed)
            index += 1

        prev = Button(
            label="<",
            style=discord.ButtonStyle.secondary,
            disabled=False
        )
        quit = Button(
            label="Quit",
            style=discord.ButtonStyle.danger,
            disabled=False
        )
        next = Button(
            label=">",
            style=discord.ButtonStyle.secondary,
            disabled=False
        )
        global page
        page = 0
        if page == 0:
            prev.disabled = True
        else: 
            prev.disabled = False
        if page == len(embeds)-1:
            next.disabled = True
        else: 
            next.disabled = False

        async def quit_callback(interaction):
            prev.disabled = True
            next.disabled = True
            quit.disabled = True
            embeds[page].color = 0xe74c3c
            await interaction.response.edit_message(embed=embeds[page], view=view)

        async def previous_callback(interaction):
            global page
            page -= 1
            if page == 0:
                prev.disabled = True
            else: 
                prev.disabled = False
            if page == len(embeds)-1:
                next.disabled = True
            else: 
                next.disabled = False
            await interaction.response.edit_message(embed=embeds[page], view=view)

        async def nextpg_callback(interaction):
            global page
            page += 1
            if page == len(embeds)-1:
                next.disabled = True
            else: 
                next.disabled = False
            if page == 0:
                prev.disabled = True
            else: 
                prev.disabled = False
            await interaction.response.edit_message(embed=embeds[page], view=view)

        async def on_timeout(interaction):
            prev.disabled = True
            next.disabled = True
            quit.disabled = True
            embeds[page].color = 0xe74c3c
            await interaction.response.edit_message(embed=embeds[page], view=view)

        quit.callback = quit_callback
        prev.callback = previous_callback
        next.callback = nextpg_callback
        view = View(timeout=30.0)
        view.add_item(prev)
        view.add_item(next)
        view.add_item(quit)
        await interaction.response.send_message(embed=embeds[page], view=view)

group3 = trade_group(name="exchange")
