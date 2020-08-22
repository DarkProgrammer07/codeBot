from discord.ext import commands

class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'🤖 beep boop!, **{str(self.client.latency)[2:4]}** ms')

def setup(client):
    client.add_cog(BasicCommands(client))