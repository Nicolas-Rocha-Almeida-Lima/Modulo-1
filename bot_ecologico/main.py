import discord
from discord.ext import commands
import random
import webbrowser
import os

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def videos(ctx):
    await ctx.send('plasticos = https://www.youtube.com/playlist?list=PL3VYgHAli5Us1pKucJbHfV-qpNyP3UIMg')
    await ctx.send('papel = https://www.youtube.com/playlist?list=PLg54jVJRnbpi8G5DbizNnlptahTlEKXwy')
    await ctx.send('vidro = https://www.youtube.com/playlist?list=PLQ9MpQTUtvpcmnHiV2Fz2bgqNd1Kd5hyD')
    await ctx.send('metal = https://www.youtube.com/playlist?list=PL6ySTcHoUdbqsZRFCTu9vwyE_8-QEdBxf')
    await ctx.send('eletronicos = https://www.youtube.com/playlist?list=PLt4LgyDsyUyX3srWugZS-EkVgs2ldbRTx')

@bot.command()
async def duração(ctx):
    await ctx.send('plastico = O plástico comum demora em média de 400 a 500 anos')
    await ctx.send('papel = varia de 3 a 6 meses')
    await ctx.send('vidro = estima-se que leve de 4 mil a 1 milhão de anos')
    await ctx.send('metal = demora de 50 a 500 anos')
    await ctx.send('eletronicos = de 100 a 500 anos')

@bot.command()
async def lixo_no_rio(ctx):
    await ctx.send('abrido documentario do rio mossoró')
    await webbrowser('https://prefeiturademossoro.com.br/noticias/trabalho-de-recuperacao-do-rio-mossoro-segue-em-andamento/14229')

@bot.command
async def quiz(ctx):
    await ctx.send('abrido quiz da CRVR')
    await webbrowser('https://crvr.com.br/jogos/quiz-da-reciclagem/')
    

bot.run('...')