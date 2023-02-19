import os
import random
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
        await ctx.send(f"@{ctx.author.name} is {cozyness}% cozy!")

        if int(cozyness) > int(self.old_cozyness):

            with open("cozy.txt", "w") as file:
                file.write(f"{user}-{cozyness}%")
                file.close()
            self.old_cozyness = cozyness

    # Project Command
    @commands.command()
    async def project(self, ctx):
        await ctx.send(f"@{ctx.author.name} - https://github.com/LemurDev/CozyBot")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
