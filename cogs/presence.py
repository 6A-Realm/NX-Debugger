import disnake
from disnake.ext import commands, tasks
import asyncio

# Cog 
class Presence(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.presence.start()

# Presence Loop
    @tasks.loop()
    async def presence(self):
        await self.client.wait_until_ready()

        await self.client.change_presence(activity = disnake.Game(name = "with switch error codes"))
        await asyncio.sleep(45)

        await self.client.change_presence(activity = disnake.Activity(type = disnake.ActivityType.watching, name = "/err <error code>"))
        await asyncio.sleep(45)

        await self.client.change_presence(activity = disnake.Game(name = "maintained by 6A"))
        await asyncio.sleep(45)


def setup(client):
    client.add_cog(Presence(client))
