import discord
from discord.ext import tasks

from cogs.music import clear_server_queue, check_queue


class Tasks:
    """
    This class contains globals `Background Task`.
    """
    def __init__(self, client):
        self.client = client

    @tasks.loop(seconds=10)
    async def check_voice_channel(self):
        voice_client = discord.utils.get(self.client.voice_clients)
        if voice_client is not None:
            members = [
                member.id for member in voice_client.channel.members
                if member.bot is not True
            ]
            if len(members) == 0:
                if check_queue() is True:
                    clear_server_queue(voice_client)
                await voice_client.disconnect()
