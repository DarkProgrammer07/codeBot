from discord.ext import commands
import json

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sendMessage(self, ctx, *, msg):
        if int(json.loads(open('config.json').read())['accessRoleID']) not in ctx.author.roles:
            return
    
        await ctx.message.channel.send(msg)
        await ctx.message.delete()
    
    @commands.command()
    async def editMessage(self, ctx, msgID, msgContent):
        if int(json.loads(open('config.json').read())['accessRoleID']) not in ctx.author.roles:
            return
        
        await ctx.message.channel.fetch_message(int(msgID)).edit(content=msgContent)

def setup(client):
    client.add_cog(Moderation(client))
