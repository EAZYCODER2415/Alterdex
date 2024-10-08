import discord
from threading import Thread
from discord.ui import Select, View, Button, Modal
from discord.ext import tasks
from discord import ui, app_commands, Member, TextChannel
import platform
import json
import random
from datetime import datetime
import time
import typing
from flask import Flask
from flask.sansio.scaffold import T_route
from config import group1
from alt import group2
from exchange import group3

app = Flask('')

@app.route('/')
def main():
    return "Alterdex Bot Status Active"

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()

keep_alive()

def load(file):
    with open(file, "r") as file:
        return json.load(file)

bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)
correct_countryball = ''
last_executed = time.time()
cooldown = 0
modal_answered = False

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
        with open("./databases/trade_history_date.json", "w") as file:
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

@bot.event
async def on_ready():
    guildcount = 0
    tree.add_command(group1)
    tree.add_command(group2)
    tree.add_command(group3)
    spawn_channel = load("./databases/channel_setup.json")
    for guild in bot.guilds:
        await tree.sync(guild=discord.Object(id=guild.id))
        print(f"{guild.id} - {guild.name}")
        try:
            print(f"Channel ID: {spawn_channel[str(guild.id)]}")
        except KeyError:
            with open("./databases/channel_setup.json", "r") as file:
                spawn_channel = json.load(file)
            spawn_channel[guild.id] = ""
            with open("./databases/channel_setup.json", "w") as file:
                json.dump(spawn_channel, file)
        guildcount += 1
    print(f"Bot successfully synced into Discord on {str(guildcount)} servers!")
    synced = await tree.sync()
    print(f"Synced {len(synced)} slash commands!")
    change_status.start()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Altballs /help"))

@bot.event
async def on_guild_join(guild):
    with open("./databases/channel_setup.json", "r") as file:
        spawn_channel = json.load(file)
    spawn_channel[guild.id] = ""
    with open("./databases/channel_setup.json", "w") as file:
        json.dump(spawn_channel, file)
    system_channel_fetch = guild.system_channel
    rules_channel_fetch = guild.rules_channel
    if system_channel_fetch != None or rules_channel_fetch != None:
        if system_channel_fetch != None:
            channel = system_channel_fetch
        elif rules_channel_fetch != None:
            channel = rules_channel_fetch
    else:
        channel_list = guild.text_channels
        channel = channel_list[random.randint(0, len(channel_list))]
    countryballs = load("./databases/countryball_list.json")
    user_completion = load("./databases/user_data.json")
    embed = discord.Embed(title=f"Thank you for inviting Alterdex to your server!", description=f'''Welcome Alterdex, a fan-made countryball collection bot that consists of "alternate universe" countrtyballs known as Altballs created by passionate Ballsdex fans. Collect them all, trade them with friends, and battle against your opponents!

Latest version **1.12.0**

`{len(countryballs["countryball"])}` Altballs to collect
`{len(bot.guilds)}` servers playing
Over more than `{len(user_completion)}`+ players worldwide!

Enjoy using Alterdex!!!''', color=0x3498db)
    embed.set_thumbnail(url=f"{bot.user.avatar.url}")
    embed.add_field(name="Time to get started!", value=f'''- Type `/config setup` to start your setup of Altball spawning.
- Then type command `/help` to get more details of the bot's usage!''')
    embed.add_field(name="Reach out to us!", value=f'''Support server: https://discord.gg/Z4dKyTBCcp
Official website: https://06e4669a-78d5-4707-a8f3-64193ea36aa4-00-3mm3mw187esqy.janeway.replit.dev/
YouTube channel: https://m.youtube.com/channel/UCZlZPQ4FZA8yj-gqDcRlixA''')
    embed.set_footer(text=f"Python {platform.python_version()} • discord.py {discord.__version__}")
    await channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    with open("./databases/channel_setup.json", "r") as file:
        spawn_channel = json.load(file)
    del spawn_channel[str(guild.id)]
    with open("./databases/channel_setup.json", "w") as file:
        json.dump(spawn_channel, file)

@bot.event 
async def on_guild_channel_delete(channel):
    with open("./databases/channel_setup.json", "r") as file:
        spawn_channel = json.load(file)
    if channel.id == spawn_channel[str(channel.guild.id)]:
        with open("./databases/channel_setup.json", "r") as file:
            spawn_channel = json.load(file)
        spawn_channel[str(channel.guild.id)] = ""
        with open("./databases/channel_setup.json", "w") as file:
            json.dump(spawn_channel, file)
    else:
        pass

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Altballs /help"))

@tree.command(name = "about", description = "View information about our bot!")
async def about(interaction):
    embed = discord.Embed(title=f"Alterdex Discord bot", description=f'''A fan-made countryball collection bot, consisting of Altballs in different alternate universes created by passionate Ballsdex fans. Collect them all, exchange with friends, and battle against other Alterdex players with Altballs!

Latest version **1.12.0**

**{len(countryballs["countryball"])}** Altballs to collect
**{len(bot.guilds)}** servers playing
Over more than **{len(user_completion)}**+ players worldwide

This bot was developed by <@1002405703991951492> and managed by <@823485434465091625>, consider contacting us.''', color=0x3498db)
    embed.set_thumbnail(url=f"{bot.user.avatar.url}")
    embed.add_field(name="Reach out to us!", value=f'''Support server: https://discord.gg/Z4dKyTBCcp
Official website: https://06e4669a-78d5-4707-a8f3-64193ea36aa4-00-3mm3mw187esqy.janeway.replit.dev/
YouTube channel: https://m.youtube.com/channel/UCZlZPQ4FZA8yj-gqDcRlixA''')
    embed.set_footer(text=f"Python {platform.python_version()} • discord.py {discord.__version__}")
    await interaction.response.send_message(embed=embed, ephemeral=False)
    
def spawn_cooldown():
    global last_executed
    global cooldown
    if last_executed + cooldown < time.time():
        last_executed = time.time()
        cooldown = 600
        return True
    return False
    
@bot.event
async def on_message(message):
    with open("./databases/channel_setup.json", "r") as file:
        spawn_channel = json.load(file)
    await bot.wait_until_ready()
    guild_id = message.guild.id
    if spawn_channel[str(guild_id)] != "":
        if not spawn_cooldown():
            pass
        else:
            channel = bot.get_channel(int(spawn_channel[str(message.guild.id)]))
            correct_countryball = random.choices(countryballs["countryball"], [0.99662162, 9.93243243, 9.86486486, 9.7972973, 9.72972973, 9.66216216, 9.59459459, 9.52702703, 9.45945946, 9.39189189, 9.32432432, 9.25675676, 9.18918919, 9.12162162, 9.05405405, 8.98648649, 8.91891892, 8.85135135, 8.78378378, 8.71621622, 8.64864865, 8.58108108, 8.51351351, 8.44594595, 8.37837838, 8.31081081, 8.24324324, 8.17567568, 8.10810811, 8.04054054, 7.97297297, 7.90540541, 7.83783784, 7.77027027, 7.7027027, 7.63513514, 7.56756757, 7.5, 7.43243243, 7.36486486, 7.2972973, 7.22972973, 7.16216216, 7.09459459, 7.02702703, 6.95945946, 6.89189189, 6.82432432, 6.75675676, 6.68918919, 6.62162162, 6.55405405, 6.48648649, 6.41891892, 6.35135135, 6.28378378, 6.21621622, 6.14864865, 6.08108108, 6.01351351, 5.94594595, 5.87837838, 5.81081081, 5.74324324, 5.67567568, 5.60810811, 5.54054054, 5.47297297, 5.40540541, 5.33783784, 5.27027027, 5.2027027, 5.13513514, 5.06756757, 5.0, 4.93243243, 4.86486486, 4.7972973, 4.72972973, 4.66216216, 4.59459459, 4.52702703, 4.45945946, 4.39189189, 4.32432432, 4.25675676, 4.18918919, 4.12162162, 4.05405405, 3.98648649, 3.91891892, 3.85135135, 3.78378378, 3.71621622, 3.64864865, 3.58108108, 3.51351351, 3.44594595, 3.37837838, 3.31081081, 3.24324324, 3.17567568, 3.10810811, 3.04054054, 2.97297297, 2.90540541, 2.83783784, 2.77027027, 2.7027027, 2.63513514, 2.56756757, 2.5, 2.43243243, 2.36486486, 2.2972973, 2.22972973, 2.16216216, 2.09459459, 2.02702703, 1.95945946, 1.89189189, 1.82432432, 1.75675676, 1.68918919, 1.62162162, 1.55405405, 1.48648649, 1.41891892, 1.35135135, 1.28378378, 1.21621622, 1.14864865, 1.08108108, 1.01351351, 0.94594595, 0.87837838, 0.81081081, 0.74324324, 0.67567568, 0.60810811, 0.54054054, 0.47297297, 0.40540541, 0.33783784, 0.27027027, 0.2027027, 0.13513514, 0.06756757])[0]
            modal_answered = False
            embed = discord.Embed(title="A wild Altball appeared!", color=0xf1c40f)
            embed.set_image(url=ball_image[f"{correct_countryball}"])
            button = Button(label="Catch Me!", style=discord.ButtonStyle.green, disabled=False)
            class guess_ball_modal(Modal, title="Guess the Altball!!"):
                countryball_answer = ui.TextInput(label="Country name", required=True, placeholder="Your guess")
                modal_answered = modal_answered
                async def on_submit(self, interaction: discord.Interaction):
                    if button.disabled != True:
                        update_user(interaction.user.id)
                        if str(self.countryball_answer).lower() == str(correct_countryball).lower():
                            button.disabled = True
                            self.modal_answered = True
                            await msg.edit(embed=embed, view=view2)
                            with open("./databases/user_data.json", "r") as file:
                                user_completion = json.load(file)
                            if correct_countryball not in user_completion[str(interaction.user.id)]:
                                with open("./databases/user_data.json", "r") as file:
                                    user_completion = json.load(file)
                                user_completion[str(interaction.user.id)].append(correct_countryball)
                                with open("./databases/user_data.json", "w") as file:
                                    json.dump(user_completion, file)
                                await interaction.response.send_message(f'''<@{interaction.user.id}> You caught **{correct_countryball}**!

This is a **new countryball** added into your collection!''')
                                last_caught = datetime.utcnow().strftime("%d/%m/%Y %H:%M %p")
                                with open("./databases/catch_date.json", "r") as file:
                                    catch_dates = json.load(file)
                                catch_dates[str(interaction.user.id)].append(last_caught)
                                with open("./databases/catch_date.json", "w") as file:
                                    json.dump(catch_dates, file)
                            else:
                                await interaction.response.send_message(f"<@{interaction.user.id}> You caught **{correct_countryball}**!")
                        else:
                            await interaction.response.send_message(f"<@{interaction.user.id}> Wrong name!")
                    else:
                        await interaction.response.send_message(f"<@{interaction.user.id}> I was already caught!")
                async def on_timeout(self):
                    button.disabled = True
                    self.modal_answered = True
                    await msg.edit(embed=embed, view=view2)
                    
            async def button_callback(interaction):
                await interaction.response.send_modal(guess_ball_modal())
            button.callback = button_callback
            view2 = View(timeout=600.0)
            view2.add_item(button)
            msg = await channel.send(embed=embed, view=view2)
    else:
        pass

@tree.command(name = "help", description = "Opens our bot's help menu!")
async def help(interaction):
    embed = discord.Embed(title=f"Alterdex help menu:", color=0x3498db)
    embed.set_thumbnail(url=f"{bot.user.avatar.url}")
    embed.add_field(name="Config", value=f'''**/config setup**: Setup spawn channel for Alterdex.
**/config disable**: Disable Altball spawning in a server.''')
    embed.add_field(name="Play", value=f'''**/alt list**: See what Altballs you or a user has.
**/alt codex**: See your current collection of the Alterdex.
**/alt count**: Count how many Altballs you have!
**/alt info**: See a specific Altball's card.
**/alt recent**: See last caught Altball.
**/alt rarity**: Shows the rarities of all Altballs..
**/alt favorite**: Set an Altball as your favorite!
**/alt donate**: Give a specific Altball to a user.''')
    embed.add_field(name="Info", value=f'''**/about**: Learn more about our bot.
**/help**: Open this help menu.''')
    embed.add_field(name="Trade", value=f'''**/exchange begin**: Begin trade with other player.
**/exchange add**: Add an Altball to the trade session.
**/exchange remove**: Remove an Altball from the trade session.
**/exchange redirect**: Navigate back to your trading session!
**/exchange history**: View your Altball trading history!''')
    await interaction.response.send_message(embed=embed, ephemeral=False)

bot.run()
# ^ PUT TOKEN HERE
