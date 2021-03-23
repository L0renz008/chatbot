#import discord
#from discord.ext import commands
#bot = commands.Bot(command_prefix = "!", description = "Bot test")

import os
import random

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents.default()
intents.members = True
#client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name} ! Bienvenue sur le serveur dédié aux restaurants !')

@bot.command(name = 'recette', help = 'Répond avec une recette au hasard.')
async def recipe(ctx):
    if ctx.author == bot.user:
        return
    recipes = ['Lasagnes ?', 'Pizza ?', 'Gâteau ?']
    response = random.choice(recipes)
    await ctx.send(response)
    
@bot.command(name = 'de', help = 'Simule un lancer de dé.')
async def roll(ctx, nombre_de_de: int, nombre_de_cote: int):
    dice = [str(random.choice(range(1, nombre_de_cote + 1)))
            for _ in range(nombre_de_de)]
    await ctx.send(', '.join(dice))
    
@bot.command(name = 'create-channel', help = 'Créer un nouveau channel textuel. Par défaut dans la catégorie : SALONS TEXTUELS.')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name, category_name = 'SALONS TEXTUELS'):
    server = ctx.guild
    existing_channel = discord.utils.get(server.channels, name = channel_name)
    category = discord.utils.get(ctx.guild.categories, name = category_name)
    print(ctx.guild.categories)
    if not category:
        await ctx.send(f'{ctx.author.mention}, cette catégorie n\'existe pas. Place le channel dans une catégorie existante.')
        return
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await server.create_text_channel(channel_name, category = category)

@bot.command(name = 'hello', help = 'Message de bienvenue et de présentation du bot.')
async def hello(ctx):
    await ctx.send('Bienvenue chez **R&L**, le restaurant où toutes les saveurs se rejoignent.\nJe suis un **serveur virtuel** du restaurant. Vous pouvez commander votre repas avec moi en tapant ce que vous désirez. Vous pouvez également me demander d\'afficher le menu avec la commande ***!menu*** ou plus spécifiquement les entrées, plats, desserts et même les vins avec les commandes respectives (***!entrees***, ***!plats***, ***!desserts***, ***!vins***).\nJe peux aussi vous conseiller pour le choix d\'un verre de vin ou d\'un dessert si vous le souhaitez.')

@bot.command(name = 'menu', help = 'Affiche le menu du restaurant')
async def menu(ctx):
    #, file = discord.File('menu_complet.jpg')
    await ctx.send('Voici le menu complet :', file = discord.File('menu_complet.jpg'))
    message = await ctx.send('Si vous souhaitez accéder aux différentes cartes, veuillez cliquer sur l\'émoji concerné :\n\t🥗 : Entrées\n\t🍔 : Plats\n\t🍪 : Desserts\n\t🍷 : Vins')
    await message.add_reaction('🥗')
    await message.add_reaction('🍔')
    await message.add_reaction('🍪')
    await message.add_reaction('🍷')
    
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id
#
    reaction, user = await bot.wait_for("reaction_add", timeout = 100, check = checkEmoji)
    if reaction.emoji == '🥗':
        await entrees.invoke(ctx)
    elif reaction.emoji == '🍔':
        await plats.invoke(ctx)
    elif reaction.emoji == '🍪':
        await desserts.invoke(ctx)
    else:
        await vins.invoke(ctx)
    

@bot.command(name = 'entrees', help = 'Affiche les entrées à la carte')
async def entrees(ctx):
    await ctx.send('Voici la carte des entrées :')

@bot.command(name = 'plats', help = 'Affiche les plats à la carte')
async def plats(ctx):
    await ctx.send('Voici le menu complet :')
    
@bot.command(name = 'desserts', help = 'Affiche les desserts à la carte')
async def desserts(ctx):
    await ctx.send('Voici le menu complet :')
    
@bot.command(name = 'vins', help = 'Affiche les plats à la carte')
async def vins(ctx):
    await ctx.send('Voici le menu complet :')

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if 'menu' in message.content:
#        await message.channel.send('Voici le menu')
#    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(f'{ctx.author.mention}, tu n\'as pas la permission de faire ça. Contacte un Admin si besoin.')


bot.run(TOKEN)


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