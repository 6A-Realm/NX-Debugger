# Public version: https://discord.com/oauth2/authorize?client_id=944063579005538354&scope=bot&permissions=309237648384
from disnake.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Invite command
    @commands.slash_command(description = "Returns bot invite.")
    async def invite(self, ctx):
        bot_invite = f"https://discord.com/oauth2/authorize?client_id={self.client.user.id}&scope=bot&permissions=309237648384"
        await ctx.send(content = bot_invite, ephemeral  = True)

def setup(client):
    client.add_cog(Invite(client))
