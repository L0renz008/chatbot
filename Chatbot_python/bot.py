#import discord
#from discord.ext import commands
#bot = commands.Bot(command_prefix = "!", description = "Bot test")

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break
    print(f'{client.user} is connected to the following server:\n'
          f'{server.name}(id: {server.id})')
    members = '\n - '.join([member.name for member in server.members])
    print(f'Server\'s Members:\n - {members}')

client.run(TOKEN)

#@bot.event
#async def on_ready():
#    print("Ready!")
#
#@bot.command()
#async def coucou(contexte):
#    await contexte.send("Coucou !")
#
#@bot.command()
#async def serverInfo(contexte):
#    server = contexte.guild
#    numberOfTextChannels = len(server.text_channels)
#    numberOfVoiceChannels = len(server.voice_channels)
#    serverDescription = server.description
#    numberOfPersons = server.member_count
#    serverName = server.name
#    message = f"Le serveur **{serverName}** contient {numberOfPersons} membres.\nLa description du serveur {serverDescription}.\nCe serveur possède {numberOfTextChannels} salon(s) écrit(s) ainsi que {numberOfVoiceChannels} salon(s) vocal.aux."
#    await contexte.send(message)
#
#@bot.command()
#async def runBot(contexte):
#    await contexte.send("Envoyez le plat que vous souhaitez cuisiner.")
#
#    def check(message):
#        return message.author == contexte.message.author and contexte.message.channel == message.channel
#    recette = await bot.wait_for("message", check = check)
#    message = await contexte.send(f"La préparation de {recette.content} va commencer. Veuillez valider avec ✅. Sinon ❌")
#    await message.add_reaction("✅")
#    await message.add_reaction("❌")
#
#    def checkEmoji(reaction, user):
#        return contexte.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
#
#    reaction, user = await bot.wait_for("reaction_add", timeout = 100, check = checkEmoji)
#
#
#bot.run("ODE4ODM3NjE0NTcxODE0OTEz.YEd39A.0nJbVuUdsroWF_kgJ53uA56VPJA")