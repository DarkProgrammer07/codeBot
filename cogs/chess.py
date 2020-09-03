from discord.ext import commands

class ChessLogic:
    def __init__(self): pass

class Chess(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Chess(client))