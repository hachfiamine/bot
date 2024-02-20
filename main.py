import discord
import os
import requests
import json
import random
from discord.ext import commands

import datetime
import time

def keep_alive():
    while True:
        requests.get("https://discord.com/api/v9/users/@me")
        time.sleep(60)

if __name__ == "__main__":
    keep_alive()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_update(before, after):
    new_role = discord.utils.get(after.roles, name="SK")

    if new_role and new_role not in before.roles:
        channel = bot.get_channel(
            1209184930093998100)  # Replace with the actual channel ID
        if channel:
            try:
                await channel.send(
                    f"Hey {after.mention}, Welcome to our clan 🎉  {new_role.name}  🎉")
            except discord.HTTPException:
                print("Failed to send the message.")

bot.run(os.getenv('TOKEN'))
