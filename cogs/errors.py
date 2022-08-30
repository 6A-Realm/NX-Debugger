from disnake.ext import commands

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You are missing required arguments.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("You were unclear with your arguments.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"I'm missing the following permissions: \n**{', '.join(error.missing_permissions)}**")
        else:
            print(f"Logical error found {error}")

def setup(client):
    client.add_cog(Errors(client))
