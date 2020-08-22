from discord.ext import commands

client = commands.Bot(command_prefix='&')
cogList = ['messageListener', 'basicCommands', 'economyControl', 'ownerAccess', 'chess']

@client.event
async def on_ready():
    print(f'Bot is alive in {len(client.guilds)} guild(s)')

if __name__ == '__main__':
    with open('.token') as tokenFile:
        token = tokenFile.read()

    for _ in cogList:
        client.load_extension('cogs.' + _)

    client.run(token)