import discord
from discord.ext import commands
import random
import webbrowser
import os

image = os.listdir(r'C:\Users\Usuário\OneDrive\Área de Trabalho\Linguagens de programação\Projeto_Koland_2026\Modulo-1\bot_meme\image')


# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def meme(ctx):
    ramdoms = random.choice(image)
    # bote o caminho da pasta image
    with open(f'image/{ramdoms}', "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def criar(ctx):
    await ctx.send('Abrido editor de meme')
    await webbrowser.open('https://www.iloveimg.com/meme-generator')

@bot.command()
async def github(ctx):
    await ctx.send("Abrido pagina do criador")
    await webbrowser("https://github.com/Nicolas-Rocha-Almeida-Lima/Modulo-1")
# Escreva a chave do seu bot
bot.run('...')