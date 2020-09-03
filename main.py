from discord.ext import commands
import os

client = commands.Bot(command_prefix='&')
cogList = [
    'messageListener',
    'basicCommands',
    'economyControl',
    'moderation',
    'ownerAccess',
    'chess'
    ]

@client.event
async def on_ready():
    print(f'Bot is alive in {len(client.guilds)} guild(s)')

if __name__ == '__main__':
    for _ in cogList:
        client.load_extension('cogs.' + _)

    client.run(os.environ['TOKEN'])
