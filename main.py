import os

import discord
from discord.ext import commands

import keep_alive

from cogs import music, suggestions, admin
from tasks import Tasks

cogs = [music, suggestions, admin]

activity = discord.Activity(type=discord.ActivityType.watching, name='que pend*jada haces')

intents = discord.Intents().all()
client = commands.Bot(command_prefix=os.environ['PREFIX'], activity=activity, intents=intents)
tk = Tasks(client)

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    tk.check_voice_channel.start()
    print("I'm ready!")


keep_alive.keep_alive()

client.run(os.environ['TOKEN'])