import os
import random
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):

    old_cozyness = 0

    def __init__(self):
        super().__init__(token=os.environ.get("TOKEN"),
                         prefix='?',
                         initial_channels=[os.environ.get("CHANNEL_NAME")])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def cozy(self, ctx: commands.Context):
        cozyness = str(random.randint(0, 100))
        user = ctx.author.name
        await ctx.send(f"@{ctx.author.name} is {cozyness}% cozy!")

        if int(cozyness) > int(self.old_cozyness):
            file = open("data/cozy.txt", "w")
            file.write(f"{user} - {cozyness}%")
            file.close()
            self.old_cozyness = cozyness


if __name__ == "__main__":
    bot = Bot()
    bot.run()
