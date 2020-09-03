from discord.ext import commands
import json

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sendMessage(self, ctx, *, msg):
        if int(json.loads(open('config.json').read())['accessRoleID']) not in [_.id for _ in ctx.author.roles]:
            return
        
        await ctx.message.delete()
        await ctx.message.channel.send(msg)
    
    @commands.command()
    async def editMessage(self, ctx, msgID, msgContent):
        if int(json.loads(open('config.json').read())['accessRoleID']) not in [_.id for _ in ctx.author.roles]:
            return
        
        _orig = await ctx.message.channel.fetch_message(int(msgID))
        await ctx.message.delete()
        await _orig.edit(content=msgContent) 

def setup(client):
    client.add_cog(Moderation(client))
