from disnake.ext import commands, tasks
from pandas import read_html
from numpy import nan
import json
import aiofiles

# Target website
url = read_html("https://switchbrew.org/wiki/Error_codes")

class NXOBD(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.scrape.start()

    @tasks.loop(hours = 12)
    async def scrape(self):

        # Define and format tables
        modules = url[1]
        codes = url[2]
        codes = codes.fillna(nan).replace([nan], [None])

        # Convert "Name" column to custom format 
        combine = json.loads(modules.set_index("Value")["Name"].to_json())
        out = {k: {"name": v} for k, v in combine.items()}

        # Add to out
        for x in range(codes.shape[0]):
            location = codes.iloc[x]
            module = str(location["Module"])
            desc = str(location["Description"])
            notes = location["Notes"]
            out[module].update([(desc, notes)])

        # Dumping json
        async with aiofiles.open("assets/api.json", mode = "w") as outfile:
            await outfile.write(json.dumps(out, indent = 4))

def setup(client):
    client.add_cog(NXOBD(client))
