import discord
from discord.ext import commands
import webbrowser

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def kodland(ctx):
    await ctx.send("Abrido pagina da web")
    await webbrowser.open('https://discordpy.readthedocs.io/en/stable/')



bot.run('...')