from discord.ext import commands
import aiosqlite
import os

class OwnerAccess(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def callEvent(self, ctx, eventName, *, args):
        self.client.dispatch(eventName, args)

        await ctx.channel.send(':thumbsup:')
            
    @commands.command()
    @commands.is_owner()
    async def showdb(self, ctx, name):
        result = '```\n'

        async with aiosqlite.connect(name) as con:
            cur = await con.cursor()

            await cur.execute('SELECT * FROM economy')
            res = await cur.fetchall()

            for _x in res:
                for _y in _x:
                    result += str(_y)
                    result += ' '
                
                result += '\n'
            result += '\n```'
        
        await ctx.send(result)

def setup(client):
    client.add_cog(OwnerAccess(client))