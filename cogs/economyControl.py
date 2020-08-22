from discord.ext import commands
import aiosqlite

class EconomyControl(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.dbName = 'database.db'
    
    @commands.Cog.listener()
    async def on_initdb(self, *args):
        args = args[0].split(' ')

        async with aiosqlite.connect(args[0]) as con:
            cur = await con.cursor()

            await cur.execute('CREATE TABLE IF NOT EXISTS economy (userID INT, money INT)')

            for _guild in self.client.guilds:

                for _member in _guild.members:
                    if not _member.bot:
                        await cur.execute('''
                        INSERT INTO economy SELECT ?, ?
                        WHERE NOT EXISTS (SELECT * FROM economy WHERE userID=?)
                        ''', (_member.id, 0, _member.id))
            
            await con.commit()

    @commands.Cog.listener()
    async def on_addMoney(self, *args):
        args = args[0].split(' ')

        async with aiosqlite.connect(self.dbName) as con:
            cur = await con.cursor()
            
            await cur.execute('SELECT * FROM economy WHERE userid = ?', (int(args[0]),))
            data = await cur.fetchone()
            newMoney = data[1] + int(args[1])

            await cur.execute('UPDATE economy SET money = ? WHERE userID = ?', (newMoney, int(args[0]),))
            
            await con.commit()

    @commands.Cog.listener()
    async def on_subMoney(self, *args):
        args = args[0].split(' ')

        async with aiosqlite.connect(self.dbName) as con:
            cur = await con.cursor()
            
            await cur.execute('SELECT * FROM economy WHERE userid = ?', (int(args[0]),))
            data = await cur.fetchone()
            newMoney = data[1] - int(args[1])

            await cur.execute('UPDATE economy SET money = ? WHERE userID = ?', (newMoney, int(args[0]),))
            
            await con.commit()

def setup(client):
    client.add_cog(EconomyControl(client))