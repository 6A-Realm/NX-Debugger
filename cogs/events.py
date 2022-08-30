from disnake.ext import commands
from aiofiles import open
import subprocess
import disnake
from os import stat, remove

class EVENTS(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Listens for report.bin files
    @commands.Cog.listener()
    async def on_message(self, message):

        # Check message and temporarily save
        if len(message.attachments) != 0 and not message.author.bot:
            attachment = message.attachments[0]
            report_bin = "assets/report"
            report_text = "assets/report.txt"
            await attachment.save(fp = report_bin)

            # Try to run report through AFE_Parser and send output as .txt
            report = await open(report_text, 'w+')
            subprocess.call(["assets/AFE_Parser", report_bin], stdout = report)

            # Check if valid/should respond
            if stat(report_text).st_size > 100:
                await message.channel.send(file = disnake.File(report_text))
            await report.close()

            # Delete all files
            remove(report_bin)
            remove(report_text)

def setup(client):
        client.add_cog(EVENTS(client))
