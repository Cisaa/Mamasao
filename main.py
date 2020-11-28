import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Mi madre es guapa?'):
        await message.channel.send('Si! Tu madre es guapisima')

    if message.content.startswith('Pero si mi madre es guapa todas las otras tambien?'):
            await message.channel.send('Si ._.')

    if message.content.startswith('AYUDA!'):
            await message.channel.send('ok te dare ayuda')
            await message.channel.send('Preguntale al bot "Mi madre es guapa?')
            await message.channel.send('Preguntale al bot "Pero si mi madre es guapa todas las otras tambien?')
            await message.channel.send(' || Hecho por Cian Pol el hijo de la Julia. ||')



client.run('NzYyMjcyMTcwOTQzOTcxMzc4.X3mvRw.63j6cSpntv8a1g1zGjmT8RvjEPs')