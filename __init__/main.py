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
            correct_countryball = random.choices(countryballs["countryball"], [0.99, 0.9926470588235294, 0.9852941176470589, 0.9779411764705882, 0.9705882352941176, 0.9632352941176471, 0.9558823529411765, 0.9485294117647058, 0.9411764705882353, 0.9338235294117647, 0.9264705882352942, 0.9191176470588235, 0.9117647058823529, 0.9044117647058824, 0.8970588235294118, 0.8897058823529411, 0.8823529411764706, 0.875, 0.8676470588235294, 0.8602941176470589, 0.8529411764705882, 0.8455882352941176, 0.8382352941176471, 0.8308823529411765, 0.8235294117647058, 0.8161764705882353, 0.8088235294117647, 0.8014705882352942, 0.7941176470588235, 0.7867647058823529, 0.7794117647058824, 0.7720588235294118, 0.7647058823529411, 0.7573529411764706, 0.75, 0.7426470588235294, 0.7352941176470589, 0.7279411764705882, 0.7205882352941176, 0.7132352941176471, 0.7058823529411765, 0.6985294117647058, 0.6911764705882353, 0.6838235294117647, 0.6764705882352942, 0.6691176470588235, 0.6617647058823529, 0.6544117647058824, 0.6470588235294118, 0.6397058823529411, 0.6323529411764706, 0.625, 0.6176470588235294, 0.6102941176470589, 0.6029411764705882, 0.5955882352941176, 0.5882352941176471, 0.5808823529411765, 0.5735294117647058, 0.5661764705882353, 0.5588235294117647, 0.5514705882352942, 0.5441176470588235, 0.5367647058823529, 0.5294117647058824, 0.5220588235294118, 0.5147058823529411, 0.5073529411764706, 0.5, 0.49264705882352944, 0.4852941176470588, 0.47794117647058826, 0.47058823529411764, 0.4632352941176471, 0.45588235294117646, 0.4485294117647059, 0.4411764705882353, 0.4338235294117647, 0.4264705882352941, 0.41911764705882354, 0.4117647058823529, 0.40441176470588236, 0.39705882352941174, 0.3897058823529412, 0.38235294117647056, 0.375, 0.36764705882352944, 0.3602941176470588, 0.35294117647058826, 0.34558823529411764, 0.3382352941176471, 0.33088235294117646, 0.3235294117647059, 0.3161764705882353, 0.3088235294117647, 0.3014705882352941, 0.29411764705882354, 0.2867647058823529, 0.27941176470588236, 0.27205882352941174, 0.2647058823529412, 0.25735294117647056, 0.25, 0.2426470588235294, 0.23529411764705882, 0.22794117647058823, 0.22058823529411764, 0.21323529411764705, 0.20588235294117646, 0.19852941176470587, 0.19117647058823528, 0.18382352941176472, 0.17647058823529413, 0.16911764705882354, 0.16176470588235295, 0.15441176470588236, 0.14705882352941177, 0.13970588235294118, 0.1323529411764706, 0.125, 0.11764705882352941, 0.11029411764705882, 0.10294117647058823, 0.09558823529411764, 0.08823529411764706, 0.08088235294117647, 0.07352941176470588, 0.0661764705882353, 0.058823529411764705, 0.051470588235294115, 0.04411764705882353, 0.03676470588235294, 0.029411764705882353, 0.022058823529411766, 0.014705882352941176, 0.007352941176470588, 0.0065])[0]
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
                        if (str(self.countryball_answer).lower() == str(correct_countryball).lower()) or (str(correct_countryball).lower() == "united kingdom") and (str(self.countryball_answer).lower() == "uk" or str(self.countryball_answer.lower() == "great britain")) or (str(correct_countryball).lower() == "2nd spanish republic") and (str(self.countryball_answer).lower() == "spain" or str(self.countryball_answer).lower() == "republic of spain") or (str(correct_countryball).lower() == "empire of croatia" and str(self.countryball_answer).lower() == "croatia") or (str(correct_countryball).lower() == "empire of algeria" and str(self.countryball_answer).lower() == "algeria") or (str(correct_countryball).lower() == "perso-mesopotamian union") and (str(self.countryball_answer).lower() == "perso mesopotamia" or str(self.countryball_answer).lower() == "persia mesopotamia" or str(self.countryball_answer).lower() == "persio mesopotamian union") or (str(correct_countryball).lower() == "greek republic" and str(self.countryball_answer).lower() == "greece") or (str(correct_countryball).lower() == "united azerbaijan" and str(self.countryball_answer).lower() == "azerbaijan") or (str(correct_countryball).lower() == "magyar fasiszta allam") and (str(self.countryball_answer).lower() == "hungarian fascists" or str(self.countryball_answer).lower() == "hungarian fascist party" or str(self.countryball_answer).lower() == "fascist hungary") or (str(correct_countryball).lower() == "black sea republic" and str(self.countryball_answer).lower() == "black sea") or (str(correct_countryball).lower() == "nordrhein-westfalen" and str(self.countryball_answer).lower() == "north rhine") or (str(correct_countryball).lower() == "rheinland-pfalz" and str(self.countryball_answer).lower() == "rhineland") or (str(correct_countryball).lower() == "atika" and str(self.countryball_answer).lower() == "athens") or (str(correct_countryball).lower() == "republic of belarus" and str(self.countryball_answer).lower() == "belarus") or (str(correct_countryball).lower() == "north macedonia" and str(self.countryball_answer).lower() == "macedonia") or (str(correct_countryball).lower() == "mecklenburg-vorpommern" and str(self.countryball_answer).lower() == "mecklenburg") or (str(correct_countryball).lower() == "republic of rome" and str(self.countryball_answer).lower() == "rome") or (str(correct_countryball).lower() == "aosta" and str(self.countryball_answer).lower() == "valle d'aosta") or (str(correct_countryball).lower() == "hungarian soviet republic" and (str(self.countryball_answer).lower() == "hsr" or str(self.countryball_answer).lower() == "hungarian socialists" or str(self.countryball_answer).lower() == "socialist hungary")) or (str(correct_countryball).lower() == "sakha republic" and (str(self.countryball_answer).lower() == "sakha" or str(self.countryball_answer).lower() == "republic of sakha")):
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
