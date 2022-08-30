from disnake.ext import commands
from re import sub
from aiohttp_requests import requests
import core.embed_creator as ec

NotFound = "Error code not found. Please make sure you have the correct error code."

class Error_Reader(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description = "Returns info on Switch (CFW) error.")
    async def err(self, ctx, *, error_code):

        # Hex support
        if error_code.startswith("0x"):
            error_hex = error_code
            error_code = int(error_code, 16)
            error_code = f"{(error_code & 0x1FF) + 2000:04}{(error_code >> 9) & 0x3FFF:04}"

        else:
            # Cleaning up error code for consistency
            error_code = sub("[^0-9]", "", error_code)

            # Convert error code to hex
            error_hex = hex((int(error_code[5:9]) << 9) + (int(error_code[:4]) - 2000))

        # Check if code is 8 digits long
        if (len(error_code)) != 8:
            return await ctx.send(NotFound)

        # Values that will be searched and embeded
        error_module = error_code[1:4]
        error_desc = error_code[7:]
        title_code = error_code[:4] + "-" + error_code[4:]

        # Async http get request
        resp = await requests.get("https://raw.githubusercontent.com/tumGER/BETCH/actions/api.json")
        response = await resp.json(content_type = "text/plain")

        # Stop if error code not found
        if not error_module in response.keys():
            return await ctx.send(NotFound)

        # Fetch module name
        module_name = response[error_module]["name"] if (response[error_module]["name"] != None) else "Unlisted"

        # Fetch error description number
        error_desc = error_desc if error_desc in response[error_module] else "1"

        # Fetch error 
        try:
            error_resp = response[error_module][error_desc]
        except KeyError:
            return await ctx.send(NotFound)

        await ec.build(self, ctx, title_code, error_hex, error_resp, module_name, error_module, error_desc)

def setup(client):
    client.add_cog(Error_Reader(client))
