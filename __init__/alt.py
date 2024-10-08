import discord
from discord.ui import Select, View, Button
from discord import app_commands, Member
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

class balls_group(app_commands.Group):

    @app_commands.command(name="list", description="See what Altballs you or somebody has!")
    async def balls_list(self, interaction, user:Member=None, sort:str=None):
        if user == None:
            user = interaction.user
        if user.bot is False:
            button1 = Button(
                label="<",
                style=discord.ButtonStyle.secondary,
                disabled=False
            )
            button = Button(
                label="Quit",
                style=discord.ButtonStyle.danger,
                disabled=False
            )
            button2 = Button(
                label=">",
                style=discord.ButtonStyle.secondary,
                disabled=False
            )
            countryballs = load("./databases/countryball_list.json")
            user_completion = load("./databases/user_data.json")
            catch_dates = load("./databases/catch_date.json")
            ball_emoji = load("./databases/emoji_ids.json")
            favorites = load("./databases/favorites_list.json")
            async def on_timeout(self):
                select.disabled = True
                button.disabled = True
                if user == None:
                    await msg2.edit(content=f"**<@{interaction.user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=view)
                else:
                    await msg2.edit(content=f"**<@{user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=view)
            async def my_callback(interaction):
                if user == None:
                    await interaction.response.send_message(f'''Altball Name: **{select.values[0]}**
        
ATK: blah blah
HP: blah blah
        
Caught on {catch_dates[str(interaction.user.id)][user_completion[str(interaction.user.id)].index(select.values[0])]}''')
                else:
                    await interaction.response.send_message(f'''Altball Name: **{select.values[0]}**
        
ATK: blah blah
HP: blah blah
        
Caught on {catch_dates[str(user.id)][user_completion[str(user.id)].index(select.values[0])]}''')
            async def prev_callback(interaction):
                global page
                page -= 1
                if page == 0:
                    button1.disabled = True
                else: 
                    button1.disabled = False
                if page == len(lists)-1:
                    button2.disabled = True
                else: 
                    button2.disabled = False
                if user == None:
                    await interaction.response.edit_message(content=f"**<@{interaction.user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
                else:
                    await interaction.response.edit_message(content=f"**<@{user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
            
            async def next_callback(interaction):
                global page
                page += 1
                if page == len(lists)-1:
                    button2.disabled = True
                else: 
                    button2.disabled = False
                if page == 0:
                    button1.disabled = True
                else: 
                    button1.disabled = False
                if user == None:
                    await interaction.response.edit_message(content=f"**<@{interaction.user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
                else:
                    await interaction.response.edit_message(content=f"**<@{user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
                
            async def button_callback(interaction):
                button.disabled = True
                button1.disabled = True
                button2.disabled = True
                select.disabled = True
                if user == None:
                    await interaction.response.edit_message(content=f"**<@{interaction.user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
                else:
                    await interaction.response.edit_message(content=f"**<@{user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page])
        
            if user == None:
                if sort == 'Most recent':
                    user_completion[str(interaction.user.id)].sort(reverse=True)
                elif sort == 'Alphabetic':
                    user_completion[str(interaction.user.id)].sort()
                else:
                    pass
                lists = []
                toIndex = 0
                maxPages = int(len(user_completion[str(interaction.user.id)]) / 20) + 1
                if (len(user_completion[str(interaction.user.id)]) % 20 == 0):
                    maxPages -= 1
                index = 0
                collectedtempnum = 0
                collectedlistdivisor = 1
                while (index < maxPages):
                    select = Select(
                        min_values=1,
                        max_values=1,
                        placeholder="Select an Altball",
                        disabled=False
                    )
                    toIndex = collectedlistdivisor * 20
                    i = collectedtempnum
                    while (i < toIndex):
                        try:
                            lower_name = user_completion[str(interaction.user.id)][i].lower()
                            if lower_name.count(" ") > 0:
                                lower_name = lower_name.replace(' ', '_')
                            else:
                                pass
                            inList = False
                            for j in range(len(favorites[str(interaction.user.id)])):
                                if (favorites[str(interaction.user.id)][j] == user_completion[str(interaction.user.id)][i]):
                                    inList = True
                            if (inList):
                                select.add_option(
                                    label=f"❤️ {user_completion[str(interaction.user.id)][i]}",
                                    value=user_completion[str(interaction.user.id)][i],
                                    emoji=str(ball_emoji[user_completion[str(interaction.user.id)][i]])
                                )
                            else:
                                select.add_option(
                                    label=user_completion[str(interaction.user.id)][i],
                                    value=user_completion[str(interaction.user.id)][i],
                                    emoji=str(ball_emoji[user_completion[str(interaction.user.id)][i]])
                                )
                            collectedtempnum += 1
                        except IndexError:
                            pass
                        i += 1
                    collectedlistdivisor += 1
                    button.callback = button_callback
                    button1.callback = prev_callback
                    button2.callback = next_callback
                    select.callback = my_callback
                    view = View(timeout=30.0)
                    view.add_item(select)
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button)
                    lists.append(view)
                    index += 1
            else:
                if sort == 'Most recent':
                    user_completion[str(user.id)].sort(reverse=True)
                elif sort == 'Alphabetic':
                    user_completion[str(user.id)].sort()
                else:
                    pass
                lists = []
                toIndex = 0
                maxPages = int(len(user_completion[str(user.id)]) / 20) + 1
                if (len(user_completion[str(user.id)]) % 20 == 0):
                    maxPages -= 1
                index = 0
                collectedtempnum = 0
                collectedlistdivisor = 1
                while (index < maxPages):
                    select = Select(
                        min_values=1,
                        max_values=1,
                        placeholder="Select an Altball",
                        disabled=False
                    )
                    toIndex = collectedlistdivisor * 20
                    i = collectedtempnum
                    while (i < toIndex):
                        try:
                            lower_name = user_completion[str(user.id)][i].lower()
                            if lower_name.count(" ") > 0:
                                lower_name = lower_name.replace(' ', '_')
                            else:
                                pass
                            inList = False
                            for j in range(len(favorites[str(user.id)])):
                                if (favorites[str(user.id)][j] == user_completion[str(user.id)][i]):
                                    inList = True
                            if (inList):
                                select.add_option(
                                    label=f"❤️ {user_completion[str(user.id)][i]}",
                                    value=user_completion[str(user.id)][i],
                                    emoji=str(ball_emoji[user_completion[str(user.id)][i]])
                                )
                            else:
                                select.add_option(
                                    label=user_completion[str(user.id)][i],
                                    value=user_completion[str(user.id)][i],
                                    emoji=str(ball_emoji[user_completion[str(user.id)][i]])
                                )
                            collectedtempnum += 1
                            collectedtempnum += 1
                        except IndexError:
                            pass
                        i += 1
                    collectedlistdivisor += 1
                    button.callback = button_callback
                    button1.callback = prev_callback
                    button2.callback = next_callback
                    select.callback = my_callback
                    view = View(timeout=30.0)
                    view.add_item(select)
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button)
                    lists.append(view)
                    index += 1
        
            global page
            page = 0
            if page == 0:
                button1.disabled = True
            else: 
                button1.disabled = False
            if page == len(lists)-1:
                button2.disabled = True
            else: 
                button2.disabled = False
            
            if user == None:
                update_user(interaction.user)
                user_completion = load("./databases/user_data.json")
                if len(user_completion[str(interaction.user.id)]) != 0:
                    msg2 = await interaction.response.send_message(f"**<@{interaction.user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page], ephemeral=False)
                else:
                    await interaction.response.send_message(f"<@{interaction.user.id}> You haven't collected any balls yet, go collect some.", ephemeral=False)
            else:
                update_user(user)
                user_completion = load("./databases/user_data.json")
                if len(user_completion[str(user.id)]) != 0:
                    msg2 = await interaction.response.send_message(f"**<@{user.id}>'s Altball list** - Page {page+1}/{maxPages}", view=lists[page], ephemeral=False)
                else:
                    await interaction.response.send_message(f"<@{user.id}> has no balls in their collection.", ephemeral=False)
        else:
            await interaction.response.send_message(f'''You cannot execute commands on:
- **Bots**
Try again.''')

    @balls_list.autocomplete("sort")
    async def sort_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        for option in ['Most recent', 'Alphabetic']:
            data.append(app_commands.Choice(name=option, value=option))  
        return data
    
    @app_commands.command(name="codex", description="Show your current completion of the Alterdex!")
    async def completion(self, interaction):
        update_user(interaction.user)
        countryballs = load("./databases/countryball_list.json")
        user_completion = load("./databases/user_data.json")
        ball_emoji = load("./databases/emoji_ids.json")
        countryballs["countryball"].sort()
        collected = []
        not_collected = []
        embeds = []
        for i in range(len(countryballs["countryball"])):
            if (countryballs["countryball"][i] in user_completion[str(interaction.user.id)]):
                collected.append(ball_emoji[countryballs["countryball"][i]])
        for i in range(len(countryballs["countryball"])):
            if (countryballs["countryball"][i] not in user_completion[str(interaction.user.id)]):
                not_collected.append(ball_emoji[countryballs["countryball"][i]])
        toIndex = 0
        maxPages = int(len(countryballs["countryball"]) / 74) + 1
        if (len(countryballs["countryball"]) % 74 == 0):
            maxPages -= 1
        collectedlist = ""
        index = 0
        collectedtemp = ""
        collectedlistnum = 0
        collectedtempnum = 0
        notcollectedlist = ""
        notcollectedtemp = ""
        notcollectedtempnum = 0
        desc = ""
        notCollectedIndex = -1
        collectedlistdivisor = 1
        notcollectedlistdivisor = 1
        global collectedListDone
        collectedListDone = False
        while (index < maxPages):
            if (len(collected) != collectedtempnum):
                collectedlist = ""
                toIndex = collectedlistdivisor * 74
                j = collectedtempnum
                while (j < toIndex):
                    try:
                        collectedlist += collected[j]
                        collectedtemp += collected[j]
                        collectedlistnum += 1
                        collectedtempnum += 1
                    except IndexError:
                        pass
                    j += 1
                if collectedlistnum == collectedtempnum:
                    collectedListDone = True
                    notCollectedIndex = index
                collectedlistdivisor += 1
            if (len(not_collected) != notcollectedtempnum and len(collected) == collectedtempnum):
                notcollectedlist = ""
                if (collectedlistnum != 0):
                    toIndex = notcollectedlistdivisor * (74 - collectedlistnum)
                else:
                    toIndex = notcollectedlistdivisor * 74
                z = notcollectedtempnum
                while (z < toIndex):
                    try:
                        notcollectedlist += not_collected[z]
                        notcollectedtemp += not_collected[z]
                        notcollectedtempnum += 1
                    except IndexError:
                        pass
                    z += 1
                notcollectedlistdivisor += 1
            desc = f'''Alterdex completion: **{round(len(collected) / len(countryballs["countryball"]), 2)}%**'''
            if index == 0:
                desc += f'''
**__Owned Altballs__**
{collectedlist}'''
            else:
                if notCollectedIndex == index or collectedtempnum != len(collected):
                    desc += f'''
{collectedlist}'''
            if collectedListDone is True:
                if notCollectedIndex == index:
                    desc += f'''
**__Other Altballs__**
{notcollectedlist}'''
                else:
                    desc += f'''
{notcollectedlist}'''
                    
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
    
    @app_commands.command(name="recent", description="See your last caught Altball!")
    async def recently_caught(self, interaction):
        update_user(interaction.user)
        user_completion = load("./databases/user_data.json")
        catch_dates = load("./databases/catch_date.json")
        await interaction.response.send_message(f'''Altball Name: **{str(user_completion[str(interaction.user.id)][-1])}**

ATK: blah blah
HP: blah blah

Caught on {str(catch_dates[str(interaction.user.id)][-1])}''', ephemeral=False)
        
    @app_commands.command(name="info", description="Shows you the info of a countryball!")
    async def ball_info(self, interaction, countryball: str):
        update_user(interaction.user)
        user_completion = load("./databases/user_data.json")
        catch_dates = load("./databases/catch_date.json")
        await interaction.response.send_message(f'''Altball Name: **{countryball}**

ATK: blah blah
HP: blah blah

Caught on {str(catch_dates[str(interaction.user.id)][user_completion[str(interaction.user.id)].index(countryball)])}''', ephemeral=False)

    @ball_info.autocomplete("countryball")
    async def countryball_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        user_completion = load("./databases/user_data.json")
        for countryball_option in user_completion[str(interaction.user.id)]:
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
    
    @app_commands.command(name="favorite", description="Set an Altball as your favorite!")
    async def favorite_set(self, interaction, countryball: str):
        update_user(interaction.user)
        favorites = load("./databases/favorites_list.json")
        ball_emoji = load("./databases/emoji_ids.json")
        inList = False
        for i in range(len(favorites[str(interaction.user.id)])):
            if (favorites[str(interaction.user.id)][i] == countryball):
                inList = True
        if (inList):
            await interaction.response.send_message(f'''{ball_emoji[countryball]} **{countryball}** is already a favorite Altball. Choose something else''', ephemeral=True)
        else:
            with open("./databases/favorites_list.json", "r") as file:
                favorites = json.load(file)
            favorites[str(interaction.user.id)].append(countryball)
            with open("./databases/favorites_list.json", "w") as file:
                json.dump(favorites, file)
            await interaction.response.send_message(f'''{ball_emoji[countryball]} **{countryball}** is now a favorite Altball.''', ephemeral=True)

    @favorite_set.autocomplete("countryball")
    async def balls_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        user_completion = load("./databases/user_data.json")
        for countryball_option in user_completion[str(interaction.user.id)]:
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
    
    @app_commands.command(name="donate", description="Gift a user one of your Altballs!")
    async def give_ball(self, interaction, user: Member, countryball: str):
        if user.bot is False and user.id != interaction.user.id:
            update_user(user)
            update_user(interaction.user)
            user_completion = load("./databases/user_data.json")
            catch_dates = load("./databases/catch_date.json")
            favorites = load("./databases/favorites_list.json")
            if countryball not in user_completion[str(user.id)]:
                countryball_location = user_completion[str(interaction.user.id)].index(countryball)
                del catch_dates[str(interaction.user.id)][int(countryball_location)]
                user_completion[str(interaction.user.id)].remove(countryball)
                user_completion[str(user.id)].append(countryball)
                last_caught = datetime.utcnow().strftime("%d/%m/%Y %H:%M %p")
                catch_dates[str(user.id)].append(last_caught)
                with open("./databases/user_data.json", "w") as file:
                    json.dump(user_completion, file)
                with open("./databases/catch_date.json", "w") as file:
                    json.dump(catch_dates, file)
                if (countryball in favorites[str(interaction.user.id)]):
                    favorites[str(interaction.user.id)].remove(countryball)
                    with open("./databases/favorites_list.json", "w") as file:
                        json.dump(favorites, file)
                await interaction.response.send_message(f"You just donated the Altball {ball_emoji[countryball]} {countryball} to <@{user.id}>!", ephemeral=False)
            else:
                await interaction.response.send_message(f"<@{user.id}> already has that Altball, donate something else!", ephemeral=False)
        else:
            await interaction.response.send_message(f'''You cannot donate Altballs to:
- **Bots**
- **Yourself**
Try again.''')

    @give_ball.autocomplete("countryball")
    async def give_ball_autocomplete(
        self,
        interaction, 
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        update_user(interaction.user)
        data = []
        user_completion = load("./databases/user_data.json")
        for countryball_option in user_completion[str(interaction.user.id)]:
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
    
    @app_commands.command(name="count", description="Count how many Altballs you have!")
    async def ballCount(self, interaction, user:Member=None):
        user_completion = load("./databases/user_data.json")
        if user == None:
            update_user(interaction.user)
            count = len(user_completion[str(interaction.user.id)])
            await interaction.response.send_message(f"You have {count} Altballs in your collection!", ephemeral=True)
        else:
            if user.bot == False:
                update_user(user)
                count = len(user_completion[str(user.id)])
                await interaction.response.send_message(f"<@{user.id}> has {count} Altballs in their collection!", ephemeral=True)
            else:
                await interaction.response.send_message(f'''You cannot use this command on:
- **Bots**
Try again.''')
                
    @app_commands.command(name="rarity", description="Shows the rarities of all Altballs.")
    async def rarityList(self, interaction):
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

group2 = balls_group(name="alt")
