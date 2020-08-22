from discord.ext import commands

class MessageListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 739538674349506642:
            if message.content.lower() == '&verify':
                await message.author.add_roles(message.guild.get_role(739346618821771286), reason='verified')
                await message.author.guild.get_channel(739341264255975466).send(f'{message.author.mention}, **whalecum to `std::code` 🐳💦**')
                await message.delete()
            else:
                await message.delete()

def setup(client):
    client.add_cog(MessageListener(client))
