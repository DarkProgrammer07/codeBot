from discord.ext import commands
import json

class MessageListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.author.name + ': ', message.content)
        if message.embeds:
            for _ in message.embeds:
                print(_.to_dict())

        if message.channel.id == json.loads(open('config.json').read())['verifyChannelID']:
            if message.content.lower() == '&verify':
                await message.author.add_roles(message.guild.get_role(739346618821771286), reason='verified')
                await message.author.guild.get_channel(json.loads(open('config.json').read())['welcomeChannelID']).send(f'{message.author.mention}, **whalecum to `Code Cave` 🐳💦**')
                await message.delete()
            else:
                await message.delete()

def setup(client):
    client.add_cog(MessageListener(client))