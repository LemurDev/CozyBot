import os
import random
import time
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()  # load env


class Bot(commands.Bot):

    # Variables
    old_cozyness = 0

    # Bot Setup
    def __init__(self):
        super().__init__(token=os.environ.get("TWITCH_ACCESS_TOKEN"),
                         prefix='?',
                         initial_channels=[os.environ.get("TWITCH_CHANNEL_NAME")])

    # On Bot Startup
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        # Clear file contents on startup
        with open("cozy.txt", 'r+') as file:
            file.truncate(0)
        with open("100_cozy.txt", 'r+') as file:
            file.truncate(0)

    # Check if any command is on cooldown
    async def event_command_error(self, ctx, error: Exception):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"@{ctx.author.name} that command is on cooldown!")

    # Cozy Command
    @commands.cooldown(rate=1, per=60, bucket=commands.Bucket.user)
    @commands.command()
    async def cozy(self, ctx: commands.Context):
        cozyness = str(random.randint(0, 100))
        user = ctx.author.name
        await ctx.send(f"@{user} is {cozyness}% cozy!")

        # If new cozyness is greater than the old value
        if int(cozyness) > int(self.old_cozyness):
            # Open cozy.txt
            with open("cozy.txt", "w") as file:
                # Write new user cozyness
                file.write(f"{user}-{cozyness}%")
                file.close()
            # Set the new greatest value
            self.old_cozyness = cozyness

            # If user cozynees is 100
            if int(cozyness) == 100:
                # Tell user in chat
                await ctx.send(f"@{user} has reached 100% cozyness!")
                # Open a new file to store username
                with open("100_cozy.txt", "w") as file:
                    # Write to text file
                    file.write(f"{user} has reached 100% cozyness!")
                    file.close()
                    time.sleep(5)
                    # Reopen it
                    f = open("100_cozy.txt", "w")
                    # Delete contents
                    f.truncate(0)
                # Reset old_cozyness
                self.old_cozyness = 0

    # Project Command
    @commands.command()
    async def project(self, ctx):
        await ctx.send(f"@{ctx.author.name} - https://github.com/LemurDev/CozyBot")

    # Lurk Command
    @commands.command()
    async def lurk(self, ctx):
        await ctx.send(f"@{ctx.author.name} is lurking under the blankets!")

    # Unlurk Command
    @commands.command()
    async def unlurk(self, ctx):
        await ctx.send(f"@{ctx.author.name} has come back from under the blankets!")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
